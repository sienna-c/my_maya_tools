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
#-------            
#LiuYang Version
import maya.cmds as cmds
def BS_Connect():
    #先选rig的base模型组， 后选abc的base模型组
    modGrp, abcGrp = cmds.ls(sl=1)  
    modAll = {m.split(':')[-1]:m for m in cmds.listRelatives(modGrp, ad=1, type='transform') if cmds.listRelatives(m, s=1)}
    abcAll = {a.split(':')[-1]:a for a in cmds.listRelatives(abcGrp, ad=1, type='transform') if cmds.listRelatives(a, s=1)}
    for mod in modAll:
        if mod in abcAll:
            try:
                cmds.blendShape(abcAll[mod], modAll[mod], origin='world', w=[0,1])
            except:
                print 'Error: Target %s does not match with base %s!!'%(abcAll[mod], modAll[mod])
