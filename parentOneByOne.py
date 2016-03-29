import maya.cmds as mc
skt = mc.ls(sl = 1)
num = len(skt)
for jts in range(0, num-1):
    mc.parent(skt[jts+1], skt[jts])
