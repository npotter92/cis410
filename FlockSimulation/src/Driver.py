__author__ = 'Nate'

from nimble import cmds
import random
from Flocker import Flocker


# Create the flock
f0 = Flocker(random.randint(-2, 2), random.randint(0, 3), random.randint(-6, 6), .1, .1, .3, "f0")
cmds.polySphere(name=f0.name, radius=0.2)

f1 = Flocker(random.randint(-2, 2), random.randint(0, 3), random.randint(-6, 6), .2, .3, .1, "f1")
cmds.polySphere(name=f1.name, radius=0.2)

f2 = Flocker(random.randint(-2, 2), random.randint(0, 3), random.randint(-6, 6), .2, .3, .1, "f2")
cmds.polySphere(name=f2.name, radius=0.2)

# Initialize time
time = 0
endTime = 480
cmds.currentTime(time)

# Initialize flock member positions
for flocker in f0.flockerArray:
    cmds.select(flocker.name)
    cmds.move(flocker.xPos, flocker.yPos, flocker.zPos)
    cmds.setKeyframe(flocker.name)

while time <= endTime:

    cmds.currentTime(time)

    for flocker in f0.flockerArray:
        flocker.updateVelocity()

    for flocker in f0.flockerArray:
        flocker.updatePostion()

        cmds.select(flocker.name)
        cmds.move(flocker.xPos, flocker.yPos, flocker.zPos)
        cmds.setKeyframe(flocker.name)

    time += 12
