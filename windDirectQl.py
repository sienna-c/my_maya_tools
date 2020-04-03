import maya.cmds as mc
def windArrow():
    wList = ['windCTRL_', 'windForQualoth_', 'arrow_', 'windTO_', 'windFROM_', 'plusL_']
    wCount = 0
    # create an empty group
    windGrp = mc.group(em=1, n=wList[0]+str(wCount))
    windGrp = mc.ls(sl=1)
    mc.select(cl=1)
    # see how many times we have used this tool
    if mc.objExists(windGrp[0]):
        wCount = str(windGrp[0])[-1]
    # create wind field and the arrow
    wField = mc.air(n=wList[1]+wCount, m=5, s=10, mxd=-1)
    wArrow = mc.curve(n=wList[2]+wCount, d=1, p=[(-1, 0, 0), (1, 0, 0), (1, 0, -6), (2, 0, -6), (0, 0, -8), (-2, 0, -6), (-1, 0, -6), (-1, 0, 0)])
    # crete the locators
    wTo = mc.spaceLocator(n=wList[3]+wCount)
    mc.move(0, 0, -10, wTo) # move it to the location
    mc.makeIdentity(wTo, apply=1, t=1) # freeze it
    wFrom = mc.spaceLocator(n=wList[4]+wCount, p=(0, 0, 0))
    mc.parent(wArrow, wFrom)
     
    mc.aimConstraint(wTo, wFrom, mo=1)
    # group them all
    mc.parent(wTo, wFrom, wField, windGrp)
    # connect xyAxis to wind    
    mc.connectAttr(wTo[0]+'.tx', wField[0]+'.dx')
    mc.connectAttr(wTo[0]+'.ty', wField[0]+'.dy')
    # parallel zAxis to localZ, connect to wind
    zAxis=mc.createNode('plusMinusAverage', n=wList[5]+wCount)
    mc.connectAttr(wTo[0]+'.tz', zAxis+'.input1D[0]')
    mc.connectAttr(wTo[0]+'Shape.lpz', zAxis+'.input1D[1]')
    mc.connectAttr(zAxis+'.output1D', wField[0]+'.dz')
