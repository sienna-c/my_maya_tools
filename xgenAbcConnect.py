import maya.cmds as mc
import xgenm as xg
import xgenm.xgGlobal as xgg
import xgenm.XgExternalAPI as xge
 
# current working folder, change folder name
projDir = mc.workspace(fullName=1)
folderSplit = projDir.split('/', 7)
folderSplit[3] = 'publish'
folderSplit[-1] = 'fcfx/fcfx/abc/'
# get fur publish folder
abcDir = '/'.join(folderSplit)
#print(abcDir)
# list all abcs
hairAbcs = mc.getFileList(fld=abcDir)
print(len(hairAbcs), hairAbcs)
prim_gui = 'SplinePrimitive'
if xgg.Maya:
 
    # palette is collection, use palettes to get collections first.
    palettes = xg.palettes()
    for palette in palettes:
        print palette
 
        # use descriptions to get description of each collection
        descriptions = xg.descriptions(palette)
        for description in descriptions:
            nameMatch = []
            allVer = {}
            print description
            
            # go through all the *.abc files in the folder, see if the description name match any file name, put it(them) in a list
            for hairAbc in hairAbcs:
                '''print hairAbc'''
                if description.split(':')[1] in hairAbc:
                    nameMatch.append(hairAbc)
                    '''print nameMatch'''
                    # put all versions of file in to a dictionary  
                    for ver in nameMatch:
                        index = int(ver[-7:-4])
                        allVer.update({ver:index})
                        print allVer
                    
                    # get the latest version
                    abcVer = max(allVer)
                    # combine to a path of that file
                    abcPath = abcDir+abcVer
                    # set attributes
                    xg.setAttr('cacheFileName', xge.prepForAttribute(abcPath.encode('ascii', 'ignore')), palette, description, prim_gui)
                    xg.setAttr('useCache', xge.prepForAttribute('True'), palette, description, prim_gui)
                    xg.setAttr('liveMode', xge.prepForAttribute('False'), palette, description, prim_gui)
                else:
                    pass
