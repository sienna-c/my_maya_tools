import maya.cmds as mc
 
mc.air(n='windForQualoth', m=5, s=10, mxd=-1)
# create an airField
mc.curve(n='arrow', d=1, p=[(-1, 0, 0), (1, 0, 0), (1, 0, -6), (2, 0, -6), (0, 0, -8), (-2, 0, -6), (-1, 0, -6), (-1, 0, 0)])
# draw an arrow
mc.spaceLocator(n='windTO')
mc.move(0, 0, -10, 'windTO')
mc.makeIdentity('windTO', apply=1, t=1)
mc.spaceLocator(n='windFROM', p=(0, 0, 0))
# create locators
 
mc.parent('arrow', 'windFROM')
# parent the arrow to FROM
mc.aimConstraint('windTO', 'windFROM', mo=1)
# aimConstaint the arrow to TO
mc.group(em=1, n='windCTRL')
mc.parent('windTO', 'windFROM', 'windForQualoth', 'windCTRL')
# group them
 
mc.connectAttr('windTO.tx', 'windForQualoth.dx')
mc.connectAttr('windTO.ty', 'windForQualoth.dy')
# connect xyAxis to wind
zAxis=mc.createNode('plusMinusAverage', n='plusL')
mc.connectAttr('windTO.tz', 'plusL.input1D[0]')
mc.connectAttr('windTOShape.lpz', 'plusL.input1D[1]')
mc.connectAttr('plusL.output1D', 'windForQualoth.dz')
# parallel zAxis to localZ, connect to wind
