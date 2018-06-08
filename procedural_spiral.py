# procedural modelling

import maya.cmds as cmds

# create a sphere
cmds.polySphere( n='mySphere', sx=5, sy=5, r=1)

# duplicate n times
for i in range(0,50):
    cmds.duplicate('mySphere')
   # cmds.move()
   # cmds.rotate(0,i*20,0)
# select spheres 

# move spheres in circle
