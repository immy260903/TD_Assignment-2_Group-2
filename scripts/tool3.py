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

workspace_path = cmds.workspace(q=True, rd=True)

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
		updated_references.append((ref_node, new_path))
	else:
		print("No new version found.")

# If there are newer versions, replace the references
if updated_references:
	print("Replacing references...")
	for ref_node, new_path in updated_references:
		try:
			cmds.file(new_path, loadReference = ref_node)
			print(f"Replaced {new_path}")
		except Exception as e:
			print(f"Error replacing {new_path}: {e}")
else:
	print("All references are up-to-date.")
