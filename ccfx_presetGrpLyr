import maya.cmds as mc

#加入了新的组名之后，要在layerC里面加入相应数量的颜色号码（1~30）
layerN=['SIM', 'inMesh', 'restMesh', 'collision_MOD', 'collision_OFFSET', 'constraint', 'spring', 'stretchRig', 'IMPORT', 'initial', 'EXPORT']
layerC=[20, 10, 29, 26, 18, 17, 9, 15, 14, 31, 4]
for eachN, eachC in zip(layerN[::-1], layerC[::-1]):
#创建层的时候是按照列表逆向创建的，这样才能使层的排序正确
    layers=mc.createDisplayLayer(e=0, n=eachN+'_DL')
    mc.setAttr(layers+'.'+'color', eachC)
 
 
if mc.objExists('OUTFIT'):
    mc.warning('The groups are right there!!')
else:
# Create group tree
    mc.group(em=1, n='OUTFIT', w=1)
    # Next branch of grp
    nextBranch=['SIM_grp', 'inMesh_grp', 'collision_grp', 'restMesh_grp', 'constraint_grp', 'spring_grp', 'initialState_grp', 'IMPORT_grp', 'EXPORT_grp', 'wrapNode_grp']
    for mainGrp in nextBranch:
        mc.group(em=1, n=mainGrp, p='OUTFIT')
    # next branch of grp
    mc.group(em=1, n='simMesh_grp', p='SIM_grp')
    mc.group(em=1, n='collider_MOD_grp', p='collision_grp')
    mc.group(em=1, n='collider_OFFSET_grp', p='collision_grp')
