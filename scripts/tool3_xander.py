import maya.cmds as cmds
import os
import re
from datetime import datetime

'''
This tool will find and load the latest version of referenced assets within a Maya scene. It will do this by:
searching the corresponding folders in the “publish” directory of the repository
checking if there is a newer version than the one in the scene
updating the scene to reference the new file.

for each referenced file within the scene:
	temporarily store the name of this file
		for every other file in this file’s directory:
			if this file’s version number is higher than the stored file’s version number:
				overwrite the stored file name with this file’s name
if the stored file name is different than the referenced file name:
	replace the scene’s referenced file name with the stored file name
reload all referenced assets
'''

def find_and_replace_new_reference_versions(*args):
	workspace_path = cmds.workspace(q=True, rd=True)
	log_text = "Scanning references at " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")

	# Get all references in the scene
	references = cmds.file(query=True, reference=True) 
	updated_references = []

	for ref in references:

		print(ref)

		# Get file path and version number of maya reference
		ref_path = cmds.referenceQuery(ref, filename=True)
		print(ref_path)

		relative_dir = os.path.relpath(os.path.dirname(ref_path), workspace_path)
		print("Scanning directory: " + relative_dir)
		maya_name = os.path.basename(ref_path)
		maya_ver = re.search(r'\.v(\d+)\.', maya_name).group(1)

		# Compare version number in maya to version numbers on disk
		new_ver = maya_ver
		new_path = ""
		absolute_dir = os.path.join(workspace_path, relative_dir)
		for root, dirs, files in os.walk(absolute_dir):
			for file in files:
				print(maya_name.split('.')[0] + " " + os.path.basename(file).split('.')[0])
				if maya_name.split('.')[0] == os.path.basename(file).split('.')[0]:
					match = re.search(r'\.v(\d+)\.', os.path.basename(file))
					if match:
						ver = match.group(1)
						if int(maya_ver) < int(ver):
							new_ver = ver
							new_path = file
			break
		
		# If a new version was found, add it to the updated references
		if new_path != "":
			print("Found new version: " + str(new_path))

			ref_node = cmds.referenceQuery(ref, referenceNode=True)
			updated_references.append((ref_node, os.path.join(absolute_dir, new_path), maya_name))
		else:
			print("No new version found.")

	# If there are newer versions, replace the references
	if updated_references:
		print("Replacing references...")
		print(updated_references)
		for ref_node, new_path, maya_name in updated_references:
			try:
				cmds.file(new_path, loadReference = ref_node)
				old_namespace = cmds.referenceQuery(ref_node, namespace=True)
				new_namespace = os.path.basename(new_path)
				new_namespace = '.'.join(new_namespace.split('.')[:-1])
				new_namespace = new_namespace.replace(".", "_")
				if cmds.namespace(exists=old_namespace) and not cmds.namespace(exists=new_namespace):
					cmds.namespace(rename=(old_namespace, new_namespace))

				print(f"Replaced {new_path}")
				log_text += f"\nUpdated reference {maya_name.split('{')[0]} to {os.path.basename(new_path)}"
			except Exception as e:
				print(f"Error replacing {new_path}: {e}")
				log_text += f"\nError updating reference {os.path.basename(new_path)}: {e}"
	else:
		print("All references are up-to-date.")
		log_text += "\nAll references are up-to-date."
	
	cmds.text("log", edit=True, label=log_text)

if cmds.window('referenceUpdater', exists = True):
    cmds.deleteUI('referenceUpdater')

cmds.window('referenceUpdater', title="Reference Updater", resizeToFitChildren=True, sizeable=False)

columnMain = cmds.columnLayout(adjustableColumn=True, columnAlign="center", rowSpacing=10)

frame = cmds.frameLayout(labelVisible=False, collapsable=False, borderVisible=False, marginHeight=10, marginWidth=10, bgc=[0.05, 0.36, 0.36])

cmds.button(label = 'Scan and Update References', command = 'find_and_replace_new_reference_versions()', bgc=[0.0, 0.5, 0.5])
cmds.text("log", label="", align="left")

# Show
cmds.showWindow('referenceUpdater')