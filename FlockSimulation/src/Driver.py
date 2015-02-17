__author__ = 'Nate'

from nimble import cmds
import random
from Flocker import Flocker
from Flocker2D import Flocker2D


# Create the flock
f0 = Flocker2D(random.randint(-3, 3), random.randint(-3, 3), random.random(), random.random(), "f0")
cmds.polySphere(name=f0.name, radius=0.2)

f1 = Flocker2D(random.randint(-3, 3), random.randint(-3, 3), random.random(), random.random(), "f1")
cmds.polySphere(name=f1.name, radius=0.2)

f2 = Flocker2D(random.randint(-3, 3), random.randint(-3, 3), random.random(), random.random(), "f2")
cmds.polySphere(name=f2.name, radius=0.2)

f3 = Flocker2D(random.randint(-3, 3), random.randint(-3, 3), random.random(), random.random(), "f3")
cmds.polySphere(name=f3.name, radius=0.2)

f4 = Flocker2D(random.randint(-3, 3), random.randint(-3, 3), random.random(), random.random(), "f4")
cmds.polySphere(name=f4.name, radius=0.2)

f5 = Flocker2D(random.randint(-3, 3), random.randint(-3, 3), random.random(), random.random(), "f5")
cmds.polySphere(name=f5.name, radius=0.2)

f6 = Flocker2D(random.randint(-3, 3), random.randint(-3, 3), random.random(), random.random(), "f6")
cmds.polySphere(name=f6.name, radius=0.2)

f7 = Flocker2D(random.randint(-3, 3), random.randint(-3, 3), random.random(), random.random(), "f7")
cmds.polySphere(name=f7.name, radius=0.2)

f8 = Flocker2D(random.randint(-3, 3), random.randint(-3, 3), random.random(), random.random(), "f8")
cmds.polySphere(name=f8.name, radius=0.2)

# Initialize time
time = 0
endTime = 480
cmds.currentTime(time)

# Initialize flock member positions
for flocker in f0.flockerArray:
    cmds.select(flocker.name)
    cmds.move(flocker.xPos, 0, flocker.zPos)
    cmds.setKeyframe(flocker.name)


while time <= endTime:

    time += 12

    for flocker in f0.flockerArray:
        flocker.updateVelocity()

    for flocker in f0.flockerArray:
        flocker.updatePostion()


    cmds.currentTime(time)
    for flocker in f0.flockerArray:
        cmds.select(flocker.name)
        cmds.move(flocker.xPos, 0, flocker.zPos)
        cmds.setKeyframe(flocker.name)
