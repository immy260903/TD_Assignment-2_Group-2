#Save and publish tool by Nathan Galang - 24570095
import os
import maya.cmds as cmds

workspace_path = cmds.workspace(q=True, rd=True)

def SaveModel():
    print('hi')

def SaveShot():
    print('hi')

# Save File Function (Parameters Filename)
def SaveFile(fileName):

    # - Search if Filename exists in wip directory
    print('hi')    
    # - If it does not exist in directory, save as Filename version 1
    # - Else if it does, check latest version and increment version number by one
    # - Save the asset with the given version number

# Publish File Function (Parameters Filename)
def PublishFile(fileName):
    print('hi')
    # - Locate publish source directory
    # - Search if Filename (without version number) exists in publish directory
    # - Make a copy save of the filename in the publish directory
    # - Create and export cache files for the savefile as .abc and .fbx
    # - Save the cache files in the corresponding abc and fbx folders as Filename of current version

# Save or Publish Tool Window Create function
def SavePublishWindow():
    # - if this window already exists, delete this window
    if cmds.window('savePublishTools', exists = True):
        cmds.deleteUI('savePublishTools')
        
    cmds.window('savePublishTools', resizeToFitChildren=True)
    # - create new window column style
    cmds.columnLayout()
    
    cmds.separator(h=10)
    cmds.text('SAVE OR PUBLISH FILE')
    cmds.text('Save Model')
    cmds.separator(h=10)

    cmds.text('asset type')
    cmds.optionMenu('assetType')
    cmds.menuItem( label='prop')
    cmds.menuItem( label='character')
    cmds.text('asset name')
    cmds.textField('assetName')
    cmds.button(label='Save', command='SaveModel()')

    cmds.separator(h=10)
    cmds.text('Save Layout, animation or lighting')
    cmds.separator(h=10)
    cmds.text('sequence name')
    cmds.textField('seqName')
    cmds.text('sequence no.')
    cmds.intField('seqNo')
    cmds.text('type')
    cmds.optionMenu('saveType')
    cmds.menuItem( label='layout')
    cmds.menuItem( label='animation')
    cmds.menuItem( label='lighting')
    cmds.button(label='Save', command='SaveShot()')

    cmds.text()
    # - Add a textfield called Filename and give it a label "File name:"
    # - Create a button called Save and make it call Save File Function with Filename as its parameter when clicked
    # - Create a button called Publish and make it call Publish File Function with Filename as its parameter when clicked



# Run Save or Publish Tool Window Create Function
SavePublishWindow()