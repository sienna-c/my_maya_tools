import maya.cmds as mc

whose = mc.ls("*:scalp_grp")
#list all "scalp_grp"

if whose[0]!="*default_a:scalp_grp":
    whose.sort(reverse=1)
    #make sure the first one is the one i want.
print(whose)
bsTarget = mc.ls(whose[1], type=['mesh'], dag=1)
#put the target shapes in a list

bsBase = mc.ls(whose[0], type=['mesh'], dag=1)
#put animated shapes in another list

for eachTarget in bsTarget:
    targetName = eachTarget.rsplit(':', 1)
    for eachBase in bsBase:
        baseName = eachBase.rsplit(':', 1)
        if targetName[1]==baseName[1]:
            #compare names, create a blendshape if they match
            mc.blendShape(eachTarget, eachBase, n='anim', w=[0, 1.0], o='world')
