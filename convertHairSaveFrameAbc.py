import maya.cmds as cmds
for eachFrame in range(1001, 1031):
    cmds.currentTime(eachFrame)#go through each frame on timeline
    cmds.select("frontal")#select the description of hair I want to convert
    dscp = cmds.ls(sl=1)#if all descriptions at the same time, skip last line. replace this line with: dscp = xg.descriptions("GBPVhqyDressHairXg")
    poly = cmds.xgmGeoRender(dscp, combineMesh=1, useWidthRamp=1, uvInTiles=1)#converted
    grp = cmds.rename("*_convert", "converted_"+str(eachFrame))#add number to the group name
    s = "-frameRange %s %s -uvWrite -writeColorSets -writeFaceSets -wholeFrameGeo -worldSpace -writeVisibility -autoSubd -writeUVSets -dataFormat ogawa -root |converted_* -file E:/GBPV_cfx_haiqinyan_dress_hair/cache/alembic/%s.abc" %(eachFrame,eachFrame,eachFrame)
    #tick the elements I want to include,name the abc file
    cmds.AbcExport(j = s)
    cmds.delete(grp)#delete the converted geo