__author__ = 'Nate'

from nimble import cmds
import random
from Flocker import Flock

def simulate(numFlockers, numFrames, alignmentWeight, cohesionWeight, separationWeight, speed, distance, in3D):

    # Create the flock
    flock = Flock(alignmentWeight, cohesionWeight, separationWeight, speed, distance)

    for i in range(numFlockers):
        xVel = random.randint(-9, 9)
        yVel = random.randint(-9, 9)
        zVel = random.randint(-9, 9)
        xPos = random.randint(-100, 100)
        yPos = random.randint(-100, 100)
        zPos = random.randint(-100, 100)
        fname = 'f' + str(i)
        if (in3D):
            flock.addFlocker(xVel, yVel, zVel, xPos, yPos, zPos, fname)
        else:
            flock.addFlocker(xVel, 0, zVel, xPos, 0, zPos, fname)

        cmds.polySphere(name=fname, radius=0.2)

    # Initialize time
    time = 0
    endTime = numFrames
    cmds.currentTime(time)

    # Initialize flock member positions
    for flocker in flock.flockers:
        cmds.select(flocker.name)
        cmds.move(flocker.xPos, flocker.yPos, flocker.zPos)
        cmds.setKeyframe(flocker.name)

    while time < endTime:

        time += 12

        for flocker in flock.flockers:
            flocker.updateVelocity(flock)

        for flocker in flock.flockers:
            flocker.updatePostion()

        cmds.currentTime(time)
        for flocker in flock.flockers:
            cmds.select(flocker.name)
            cmds.move(flocker.xPos, flocker.yPos, flocker.zPos)
            cmds.setKeyframe(flocker.name)
