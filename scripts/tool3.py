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

# Get all references in the scene
references = cmds.file(query=True, reference=True) 
updated_references = []

for ref in references:

	# Get file path and version number of maya reference
	ref_path = cmds.referenceQuery(ref, filename=True)
	dir = os.path.dirname(ref_path)
	maya_name = os.path.basename(ref_path)
	maya_ver = re.search(r'\.v(\d+)\.', maya_name).group(1)
	print(maya_ver)

	# Compare version number in maya to version numbers on disk
	new_ver = ""
	new_file = ""
	for root, dirs, files in os.walk(dir):
		for file in files:
			match = re.search(r'\.v(\d+)\.', os.path.basename(file))
			if match:
				ver = match.group(1)
				if int(maya_ver) < int(ver):
					new_ver = ver
					new_file = file
	
	# If a new version was found, add it to the updated references
	if new_file != "":
		updated_references.append(os.path.join(dir, new_file))

# If there are newer versions, replace the references
if updated_references:
	print("Newer versions found. Replacing references...")
else:
	print("All references are up-to-date.")
