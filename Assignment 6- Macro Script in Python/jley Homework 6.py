import maya.cmds as cmds

cmds.polySphere(r=3, sx=20, sy=20, ax=[0, 1, 0])
cmds.move(0, 3, 0)

# create middle sphere
cmds.polySphere(r=2, sx=20, sy=20, ax=[0, 1, 0])
cmds.move(0, 7, 0)

# create head sphere
cmds.polySphere(r=1, sx=20, sy=20, ax=[0, 1, 0])
cmds.move(0, 9.5, 0)

# create nose
cmds.polyCone(r=0.25,h=0.5,ax=[0,1,0])
cmds.move(0,9.5,1.175)
cmds.rotate('90deg',0,0)

# create eyes
cmds.polySphere(r=0.25,ax=[0,1,0])
cmds.move(-.4,9.93,0.6)

cmds.polySphere(r=0.25,ax=[0,1,0])
cmds.move(.4,9.93,0.6)

# create arms
cmds.polyCylinder(r=0.25,h=3,ax=[0,1,0])
cmds.move(-3,7.85,0)
cmds.rotate(0,0,'73deg')

cmds.polyCylinder(r=0.25,h=3,ax=[0,1,0])
cmds.move(3,7.85,0)
cmds.rotate(0,0,'-73deg')

