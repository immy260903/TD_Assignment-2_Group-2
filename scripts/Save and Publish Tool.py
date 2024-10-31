#Save and publish tool by Nathan Galang - 24570095
import os
import maya.cmds as cmds

# reference the workspace path so that the tool can function on anyone's device
workspace_path = cmds.workspace(q=True, rd=True)

def SaveModel():
    # grab values from the tool window
    assetType = cmds.optionMenu('assetType', query = True, value = True)
    assetName = cmds.textField('assetName', query = True, text = True)
    print(assetType)
    print(assetName)
    # form a string of the path for the asset's directory
    assetDir = workspace_path + "wip/assets/" + assetType + "/" + assetName
    # if it doesn't exist, then create relevant directories
    if os.path.exists(assetDir) == False:
        os.mkdir(assetDir)
        os.mkdir(assetDir + "/model")
        os.mkdir(assetDir + "/model/source")
    # form a string of the path where the file will be saved
    dirPath = workspace_path + "wip/assets/" + assetType + "/" + assetName + "/model/source/"
    print(dirPath)
    # finalise filename 
    fileName = assetName + "_model"
    # run SaveFile to save the file in the given path 
    SaveFile(fileName, dirPath)


def SaveShot():
    # grab values from the tool window
    sequenceName = cmds.textField('seqName', query = True, text = True)
    # set shot number value to follow '000' format
    shotNo = str(cmds.intField('shotNo', query=True, value = True)).rjust(3, '0')
    shotName = sequenceName + "_" + shotNo
    saveType = cmds.optionMenu('saveType', query = True, value = True)
    print(sequenceName)
    print(shotName)
    print(saveType)
    # form a string of the path for the sequence's directory
    sequenceDir = workspace_path + "wip/sequence/" + sequenceName
    # if it doesn't exist, then create relevant directories
    if os.path.exists(sequenceDir) == False:
        os.mkdir(sequenceDir)
    # form a string of the path for the shot's directory
    shotDir = sequenceDir + "/" + shotName
    # if it doesn't exist, then create relevant directories
    if os.path.exists(shotDir) == False:
        os.mkdir(shotDir)
        os.mkdir(shotDir + "/" + saveType)
        os.mkdir(shotDir + "/" + saveType + "/source")
    # finalise filename and form a string of the path where the file will be saved
    shotFileDirPath = shotDir + "/" + saveType + "/source/"
    fileName = shotName + "_" + saveType
    print(shotFileDirPath)
    print(fileName)
    # run SaveFile to save the file in the given path 
    SaveFile(fileName, shotFileDirPath)

# Save File Function (Parameters Filename, Directory)
def SaveFile(fileName, directory):
    # find files in the given directory
    dir_list = os.listdir(directory)
    print(len(dir_list))
    # if there is none, immediately give it version 1
    if len(dir_list) <= 0:
        fileName += ".v001"

    # else look for filenames with the same asset name
    else:
        sameFileFound = False
        highestVer = 1
        for x in dir_list:
            if fileName == x.split(".")[0]:
                sameFileFound = True
                break
        
        # if there is a file with the same name, find the highest version
        if sameFileFound == True:
            for x in dir_list:
                if fileName == x.split(".")[-2]:
                    fileVer = x.split(".")[-1]
                    if highestVer < int(fileVer.split("v")[-1]):
                        highestVer = int(fileVer.split("v")[-1])
            highestVer += 1 
        
        print(sameFileFound)
        # increment the highest version by one and give that version to the filename
        fileVer = ".v" + str(highestVer).rjust(3, '0')
        fileName += fileVer
     
    finalDir = directory + fileName
    print(finalDir)
    # - Save the asset with the given version number
    cmds.select(all=True)
    cmds.file(finalDir, f=True, type="mayaBinary",es=True)
    cmds.select( clear=True )

def PublishAsset():
    # grab values from the tool window
    assetType = cmds.optionMenu('assetType', query = True, value = True)
    assetName = cmds.textField('assetName', query = True, text = True)
    assetVer = str(cmds.intField('assetVer', query = True, value = True)).rjust(3, '0')
    print(assetType)
    print(assetName)
    print(assetVer)
    # form a string of the path for the asset's directory
    assetDir = workspace_path + "publish/assets/" + assetType + "/" + assetName
    # if it doesn't exist, then create relevant directories
    if os.path.exists(assetDir) == False:
        os.mkdir(assetDir)
        os.mkdir(assetDir + "/model")
        os.mkdir(assetDir + "/model/source")

    # form a string of the path for the asset's directory and finalise filename
    dirPath = assetDir + "/model/source/"
    fileName = assetName + "_" + assetType + ".v" + assetVer
    finalPath = dirPath + fileName
    
    # form a string for the cache directory
    cacheDir = assetDir + "/model/caches"
    # make the cache directories if they don't exist
    if os.path.exists(cacheDir) == False:
        os.mkdir(cacheDir)
        os.mkdir(cacheDir + "/fbx")
        os.mkdir(cacheDir + "/usd")
    
    # make strings for the fbx and usd cache file paths to export in
    fbxPath = cacheDir + "/fbx/" + fileName
    usdPath = cacheDir + "/usd/" + fileName
    print(finalPath)
    print(fbxPath)
    print(usdPath)


    # publish the asset in the given path, as well as export cache in fbx and usd 
    cmds.select(all=True)
    cmds.file(finalPath, f=True, type="mayaBinary",es=True)
    cmds.file(fbxPath, f=True, type="FBX export",es=True)
    cmds.file(usdPath, f=True, type="USD export",es=True)
    cmds.select( clear=True)


def PublishLayout():
    # grab values from the tool window
    sequenceName = cmds.textField('layoutSeqName', query = True, text = True)
    shotNo = str(cmds.intField('layoutShotNo', query=True, value = True)).rjust(3, '0')
    shotName = sequenceName + "_" + shotNo
    layoutVer = str(cmds.intField('layoutVer', query = True, value = True)).rjust(3, '0')
    print(sequenceName)
    print(shotName)
    # form a string of the path for the sequence's directory
    sequenceDir = workspace_path + "publish/sequence/" + sequenceName
    # if it doesn't exist, then create relevant directories
    if os.path.exists(sequenceDir) == False:
        os.mkdir(sequenceDir)
    # form a string of the path for the shot's directory
    shotDir = sequenceDir + "/" + shotName
    # if it doesn't exist, then create relevant directories
    if os.path.exists(shotDir) == False:
        os.mkdir(shotDir)
        os.mkdir(shotDir + "/layout")
        os.mkdir(shotDir + "/layout/source")

    # form a string of the path for the asset's directory and finalise filename
    shotFileDirPath = shotDir + "/layout/source/"
    fileName = shotName + "_layout.v" + layoutVer
    filePath = shotFileDirPath + fileName
    print(filePath)

    # publish the layout file
    cmds.select(all=True)
    cmds.file(filePath, f=True, type="mayaBinary",es=True)
    cmds.select( clear=True )

    # create a string for the cache filename
    cacheFileName = shotName + "_cam_layout.v" + layoutVer
    # form a string for the cache directory
    cacheDir = shotDir + "/layout/cache/"
    # make the cache directories if they don't exist
    if os.path.exists(cacheDir) == False:
        os.mkdir(cacheDir)
        os.mkdir(cacheDir + "/fbx")
        os.mkdir(cacheDir + "/usd")
    # make strings for the fbx and usd cache file paths to export in
    fbxPath = cacheDir + "/fbx/" + cacheFileName
    usdPath = cacheDir + "/usd/" + cacheFileName

    # export all cameras in the layout as cache fbx and usd
    layoutCameras = cmds.ls(cameras=True)
    for x in layoutCameras:
        cmds.select(x)
    cmds.file(fbxPath, f=True, type="FBX export",es=True)
    cmds.file(usdPath, f=True, type="USD export",es=True)
    cmds.select( clear=True)

# functions the same as PublishLayout, except for exporting animation cache files 
def PublishAnim():
    sequenceName = cmds.textField('animSeqName', query = True, text = True)
    shotNo = str(cmds.intField('animShotNo', query=True, value = True)).rjust(3, '0')
    shotName = sequenceName + "_" + shotNo
    layoutVer = str(cmds.intField('animVer', query = True, value = True)).rjust(3, '0')
    print(sequenceName)
    print(shotName)

    sequenceDir = workspace_path + "publish/sequence/" + sequenceName
    if os.path.exists(sequenceDir) == False:
        os.mkdir(sequenceDir)
    shotDir = sequenceDir + "/" + shotName
    if os.path.exists(shotDir) == False:
        os.mkdir(shotDir)
        os.mkdir(shotDir + "/animation")
        os.mkdir(shotDir + "/animation/source")
    shotFileDirPath = shotDir + "/animation/source/"
    fileName = shotName + "_animation.v" + layoutVer
    filePath = shotFileDirPath + fileName
    print(filePath)

    cmds.select(all=True)
    cmds.file(filePath, f=True, type="mayaBinary",es=True)
    cmds.select( clear=True)
    
    # create a string of the cache directory
    cacheDir = shotDir + "/animation/cache/"
    # create the directories if they don't exist
    if os.path.exists(cacheDir) == False:
        os.mkdir(cacheDir)
        os.mkdir(cacheDir + "/fbx")
        os.mkdir(cacheDir + "/usd")

    # iterate through each character object animation in the scene and export cache as fbx and usd
    characters = cmds.listRelatives('character')
    for character in characters:
        cacheFileName = shotName + "_" + character + "_layout.v" + layoutVer
        fbxPath = cacheDir + "/fbx/" + cacheFileName
        usdPath = cacheDir + "/usd/" + cacheFileName
        cmds.select(character)
        cmds.file(fbxPath, f=True, type="FBX export",es=True)
        cmds.file(usdPath, f=True, type="USD export",es=True)

    # same with props
    props = cmds.listRelatives('prop')
    for prop in props:
        cacheFileName = shotName + "_" + prop + "_layout.v" + layoutVer
        fbxPath = cacheDir + "/fbx/" + cacheFileName
        usdPath = cacheDir + "/usd/" + cacheFileName
        cmds.select(prop)
        cmds.file(fbxPath, f=True, type="FBX export",es=True)
        cmds.file(usdPath, f=True, type="USD export",es=True)

    cmds.select( clear=True)

    


def SaveOrPublishWindow():
    # - if this window already exists, delete this window
    if cmds.window('saveOrPublishTools', exists = True):
        cmds.deleteUI('saveOrPublishTools')
        
    cmds.window('saveOrPublishTools', resizeToFitChildren=True)
    # - create new window column style
    cmds.columnLayout('baseLayout',adj=True)
    # Displays a window for the user to choose either to save or publish a file.
    cmds.separator(h=10)
    cmds.text('SAVE AND PUBLISH TOOL')
    cmds.text('A tool that helps you save/publish your assets files.')
    cmds.separator(h=10)
    cmds.button(label='Save', command='SaveWindow()')
    cmds.separator(h=10)
    cmds.button(label='Publish', command='PublishWindow()')

    cmds.showWindow('saveOrPublishTools')

# Save Tool Window Create function
def SaveWindow():
    # - if this window already exists, delete this window
    if cmds.window('saveTools', exists = True):
        cmds.deleteUI('saveTools')
        
    cmds.window('saveTools', resizeToFitChildren=True)
    # - create new window column style
    cmds.columnLayout('baseLayout',adj=True)
    
    # Save model section - asks for asset type and name of asset
    cmds.separator(h=10)
    cmds.text('SAVE FILE')
    cmds.text('Save Model')
    cmds.separator(h=10)

    cmds.text('Asset type:')
    cmds.optionMenu('assetType')
    cmds.menuItem( label='prop')
    cmds.menuItem( label='character')
    cmds.menuItem( label='set')
    cmds.menuItem( label='setPiece')
    cmds.text('Asset name:')
    cmds.textField('assetName')
    cmds.separator(h=10)

    cmds.button(label='Save Asset', command='SaveModel()')
    # Save Layout, animation or lighting section - asks for sequence name, shot number and save type
    cmds.separator(h=30)
    cmds.text('Save Layout, animation or lighting')
    cmds.separator(h=10)
    cmds.text('Sequence name:')
    cmds.textField('seqName')
    cmds.text('Shot number:')
    cmds.intField('shotNo')
    cmds.text('Type: ')
    cmds.separator(h=10)
    cmds.optionMenu('saveType')
    cmds.menuItem( label='layout')
    cmds.menuItem( label='animation')
    cmds.menuItem( label='lighting')
    cmds.separator(h=10)

    cmds.button(label='Save Shot', command='SaveShot()')

    cmds.showWindow('saveTools')

# Publish Tool Window Create function
def PublishWindow():
    # - if this window already exists, delete this window
    if cmds.window('publishTools', exists = True):
        cmds.deleteUI('publishTools')
        
    cmds.window('publishTools', resizeToFitChildren=True)
    # - create new window column style
    cmds.columnLayout('baseLayout',adj=True)

    # Publish Asset section - asks for asset type, asset name and asset version
    cmds.separator(h=10)
    cmds.text('PUBLISH FILE')
    cmds.text('Publish Asset')
    cmds.separator(h=10)

    cmds.text('Asset type:')
    cmds.optionMenu('assetType')
    cmds.menuItem( label='prop')
    cmds.menuItem( label='character')
    cmds.menuItem( label='set')
    cmds.menuItem( label='setPiece')
    cmds.text('Asset name:')
    cmds.textField('assetName')
    cmds.text('Asset version:')
    cmds.intField('assetVer')
    cmds.separator(h=10)

    cmds.button(label='Publish Asset', command='PublishAsset()')

    # Publish Layout section - asks for sequence name, shot number and layout version

    cmds.separator(h=10)
    cmds.text('Publish Layout')
    cmds.separator(h=10)
    cmds.text('Sequence name:')
    cmds.textField('layoutSeqName')
    cmds.text('Shot number:')
    cmds.intField('layoutShotNo')
    cmds.text('Layout version:')
    cmds.intField('layoutVer')
    cmds.separator(h=10)

    cmds.separator(h=10)

    cmds.button(label='Publish Layout', command='PublishLayout()')

    # Publish Animation section - asks for sequence name, shot number and animation version

    cmds.separator(h=10)
    cmds.text('Publish Animation')
    cmds.separator(h=10)
    cmds.text('Sequence name:')
    cmds.textField('animSeqName')
    cmds.text('Shot number:')
    cmds.intField('animShotNo')
    cmds.text('Animation version:')
    cmds.intField('animVer')
    cmds.separator(h=10)

    cmds.separator(h=10)

    cmds.button(label='Publish Animation', command='PublishAnim()')

    cmds.showWindow('publishTools')



# Run Save or Publish Tool Window Create Function
SaveOrPublishWindow()