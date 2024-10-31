#Save and publish tool by Nathan Galang - 24570095
import os
import maya.cmds as cmds

workspace_path = cmds.workspace(q=True, rd=True)

def SaveModel():
    assetType = cmds.optionMenu('assetType', query = True, value = True)
    assetName = cmds.textField('assetName', query = True, text = True)
    print(assetType)
    print(assetName)
    assetDir = workspace_path + "wip/assets/" + assetType + "/" + assetName
    if os.path.exists(assetDir) == False:
        os.mkdir(assetDir)
        os.mkdir(assetDir + "/model")
        os.mkdir(assetDir + "/model/source")
    dirPath = workspace_path + "wip/assets/" + assetType + "/" + assetName + "/model/source/"
    print(dirPath)
    fileName = assetName + "_model"
    SaveFile(fileName, dirPath)


def SaveShot():
    sequenceName = cmds.textField('seqName', query = True, text = True)
    shotNo = str(cmds.intField('shotNo', query=True, value = True)).rjust(3, '0')
    shotName = sequenceName + "_" + shotNo
    saveType = cmds.optionMenu('saveType', query = True, value = True)
    print(sequenceName)
    print(shotName)
    print(saveType)
    sequenceDir = workspace_path + "wip/sequence/" + sequenceName
    if os.path.exists(sequenceDir) == False:
        os.mkdir(sequenceDir)
    shotDir = sequenceDir + "/" + shotName
    if os.path.exists(shotDir) == False:
        os.mkdir(shotDir)
        os.mkdir(shotDir + "/" + saveType)
        os.mkdir(shotDir + "/" + saveType + "/source")
    shotFileDirPath = shotDir + "/" + saveType + "/source/"
    fileName = shotName + "_" + saveType
    print(shotFileDirPath)
    print(fileName)
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
            if fileName == x.split(".")[-2]:
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
    assetType = cmds.optionMenu('assetType', query = True, value = True)
    assetName = cmds.textField('assetName', query = True, text = True)
    assetVer = str(cmds.intField('assetVer', query = True, value = True)).rjust(3, '0')
    print(assetType)
    print(assetName)
    print(assetVer)
    assetDir = workspace_path + "publish/assets/" + assetType + "/" + assetName
    if os.path.exists(assetDir) == False:
        os.mkdir(assetDir)
        os.mkdir(assetDir + "/model")
        os.mkdir(assetDir + "/model/source")
    dirPath = assetDir + "/model/source/"
    fileName = assetName + "_" + assetType + ".v" + assetVer
    finalPath = dirPath + fileName
    
    cacheDir = assetDir + "/model/caches"
    if os.path.exists(cacheDir) == False:
        os.mkdir(cacheDir)
        os.mkdir(cacheDir + "/fbx")
        os.mkdir(cacheDir + "/usd")
    fbxPath = cacheDir + "/fbx/" + fileName
    usdPath = cacheDir + "/usd/" + fileName
    print(finalPath)
    print(fbxPath)
    print(usdPath)
    
    cmds.select(all=True)
    cmds.file(finalPath, f=True, type="mayaBinary",es=True)
    cmds.file(fbxPath, f=True, type="FBX export",es=True)
    cmds.file(usdPath, f=True, type="USD export",es=True)
    cmds.select( clear=True )

# Publish File Function (Parameters Filename)
def PublishLayout():
    sequenceName = cmds.textField('layoutSeqName', query = True, text = True)
    shotNo = str(cmds.intField('layoutShotNo', query=True, value = True)).rjust(3, '0')
    shotName = sequenceName + "_" + shotNo
    layoutVer = str(cmds.intField('layoutVer', query = True, value = True)).rjust(3, '0')
    print(sequenceName)
    print(shotName)

    sequenceDir = workspace_path + "publish/sequence/" + sequenceName
    if os.path.exists(sequenceDir) == False:
        os.mkdir(sequenceDir)
    shotDir = sequenceDir + "/" + shotName
    if os.path.exists(shotDir) == False:
        os.mkdir(shotDir)
        os.mkdir(shotDir + "/layout")
        os.mkdir(shotDir + "/layout/source")
    shotFileDirPath = shotDir + "/layout/source/"
    fileName = shotName + "_layout.v" + layoutVer
    filePath = shotFileDirPath + fileName
    print(filePath)

    cmds.select(all=True)
    cmds.file(filePath, f=True, type="mayaBinary",es=True)
    cmds.select( clear=True )
    cacheFileName = shotName + "_cam_layout.v" + layoutVer
    cacheDir = shotDir + "/layout/cache/"
    if os.path.exists(cacheDir) == False:
        os.mkdir(cacheDir)
        os.mkdir(cacheDir + "/fbx")
        os.mkdir(cacheDir + "/usd")
    fbxPath = cacheDir + "/fbx/" + cacheFileName
    usdPath = cacheDir + "/usd/" + cacheFileName

    layoutCameras = cmds.ls(cameras=True)
    for x in layoutCameras:
        cmds.select(x)
    cmds.file(fbxPath, f=True, type="FBX export",es=True)
    cmds.file(usdPath, f=True, type="USD export",es=True)
    cmds.select( clear=True)

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
    
    cacheDir = shotDir + "/animation/cache/"
    if os.path.exists(cacheDir) == False:
        os.mkdir(cacheDir)
        os.mkdir(cacheDir + "/fbx")
        os.mkdir(cacheDir + "/usd")

    characters = cmds.listRelatives('character')
    for character in characters:
        cacheFileName = shotName + "_" + character + "_layout.v" + layoutVer
        fbxPath = cacheDir + "/fbx/" + cacheFileName
        usdPath = cacheDir + "/usd/" + cacheFileName
        cmds.select(character)
        cmds.file(fbxPath, f=True, type="FBX export",es=True)
        cmds.file(usdPath, f=True, type="USD export",es=True)

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

    cmds.separator(h=10)
    cmds.text('SAVE AND PUBLISH TOOL')
    cmds.text('A tool that helps you save/publish your assets files.')
    cmds.separator(h=10)
    cmds.button(label='Save', command='SaveWindow()')
    cmds.separator(h=10)
    cmds.button(label='Publish', command='PublishWindow()')

    cmds.showWindow('saveOrPublishTools')

# Save or Publish Tool Window Create function
def SaveWindow():
    # - if this window already exists, delete this window
    if cmds.window('saveTools', exists = True):
        cmds.deleteUI('saveTools')
        
    cmds.window('saveTools', resizeToFitChildren=True)
    # - create new window column style
    cmds.columnLayout('baseLayout',adj=True)
    
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

    # - Add a textfield called Filename and give it a label "File name:"
    # - Create a button called Save and make it call Save File Function with Filename as its parameter when clicked
    # - Create a button called Publish and make it call Publish File Function with Filename as its parameter when clicked

# Save or Publish Tool Window Create function
def PublishWindow():
    # - if this window already exists, delete this window
    if cmds.window('publishTools', exists = True):
        cmds.deleteUI('publishTools')
        
    cmds.window('publishTools', resizeToFitChildren=True)
    # - create new window column style
    cmds.columnLayout('baseLayout',adj=True)

    cmds.separator(h=10)
    cmds.text('PUBLISH FILE')
    cmds.text('Save Asset')
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

    cmds.separator(h=10)
    cmds.text('Save Layout')
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

    cmds.separator(h=10)
    cmds.text('Save Animation')
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