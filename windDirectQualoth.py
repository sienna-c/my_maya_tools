import maya.cmds as mc
  
mc.curve(n='arrow', d=1, p=[(-1, 0, 0), (1, 0, 0), (1, 0, -6), (2, 0, -6), (0, 0, -8), (-2, 0, -6), (-1, 0, -6), (-1, 0, 0)])
#draw an arrow
mc.spaceLocator(n='windTO')
mc.move(0, 0, -10, 'windTO')
mc.makeIdentity('windTO', apply=1, t=1)
mc.spaceLocator(n='windFROM', p=(0, 0, 0))
# create locators
mc.parent('arrow', 'windFROM')
# parent the arrow to FROM
mc.aimConstraint('windTO', 'windFROM', mo=1)
# aimConstaint the arrow to TO
