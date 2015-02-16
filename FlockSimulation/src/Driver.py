__author__ = 'Nate'

from nimble import cmds
import random
from Flocker import Flocker
from Flocker2D import Flocker2D


# Create the flock
f0 = Flocker2D(1, 0, .1, .3, "f0")
cmds.polySphere(name=f0.name, radius=0.2)

f1 = Flocker2D(0, 0, .2, .1, "f1")
cmds.polySphere(name=f1.name, radius=0.2)

f2 = Flocker2D(-1, 1, .2, -.1, "f2")
cmds.polySphere(name=f2.name, radius=0.2)

# Initialize time
time = 0
endTime = 121
cmds.currentTime(time)

# Initialize flock member positions
for flocker in f0.flockerArray:
    cmds.select(flocker.name)
    cmds.move(flocker.xPos, 0, flocker.zPos)
    cmds.setKeyframe(flocker.name)

time = 1

while time <= endTime:


    for flocker in f0.flockerArray:
        print(flocker.name, flocker.xVel)
        flocker.updateVelocity()
        print (flocker.name, flocker.xVel)

    for flocker in f0.flockerArray:
        flocker.updatePostion()


    cmds.currentTime(time)
    for flocker in f0.flockerArray:
        cmds.select(flocker.name)
        cmds.move(flocker.xPos, 0, flocker.zPos)
        cmds.setKeyframe(flocker.name)

    time += 6
