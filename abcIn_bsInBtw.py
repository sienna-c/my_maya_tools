import maya.cmds as cmds

start = 1132
end = 1200

for eachFrame in range(start, end+1):#import all abc
    fileLoc = "E:/GBPV_cfx_haiqinyan_dress_hair/cache/alembic/"
    cmds.AbcImport(fileLoc+str(eachFrame)+".abc")

allCache = cmds.ls("converted_*")
cmds.blendShape(allCache[-1], allCache[0], n="blendFrames")
cmds.currentTime(start-1000)
cmds.setKeyframe("blendFrames."+allCache[-1], v=0, itt="linear", ott="linear")
cmds.currentTime(end-1000)
cmds.setKeyframe("blendFrames."+allCache[-1], v=1, itt="linear", ott="linear")

multi = 0
for nextFrame in range(start-1000+1, end-1000):
    frameAt = cmds.currentTime(nextFrame)
    multi = multi+1
    ibv = round(1.0/(end-start)*multi,3)
    #print ibv
    cmds.blendShape("blendFrames", edit=True, ib=True, tc=True, ibt="absolute", t=(allCache[0], 0, "converted_"+str(nextFrame+1000), ibv))
