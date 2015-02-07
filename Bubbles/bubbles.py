"""
bubbles.py
Script to procedurally generate and animate multiple bubbles rising
with random initial conditions.
Author: Nate Potter
"""
from nimble import cmds
import random


def bubbleRise(bubble):
    """
    Animates the rising motion of one bubble object at a random time.
    Parameters:
        bubble - string name of the polySphere object
    """

    time = random.randint(0, 168)

    cmds.select(bubble)

    cmds.currentTime(time)
    cmds.setAttr(bubble+'.visibility', 1)
    cmds.scale(1, 0.32, 1)
    cmds.setKeyframe(bubble)
    time += 24

    cmds.currentTime(time)
    cmds.move(0.25, 0.9, -0.25, relative=True)
    cmds.scale(1, 0.55, 1)
    cmds.setKeyframe(bubble)
    time += 24

    cmds.currentTime(time)
    cmds.move(-0.75, 4.2, 0.75, relative=True)
    cmds.scale(1, 0.8, 1)
    cmds.setKeyframe(bubble)
    time += 24

    cmds.currentTime(time)
    cmds.move(1, 8, -1, relative=True)
    cmds.scale(1, 1, 1)
    cmds.setKeyframe(bubble)

    cmds.currentTime(time+1)
    cmds.setAttr(bubble+'.visibility', 0)
    cmds.setKeyframe(bubble)

# create the 'master bubble'
r = random.randint(1, 10) / 20
c = cmds.polySphere(name='bubble', radius=r)[0]
cmds.currentTime(0)
cmds.select('bubble')
cmds.setAttr('bubble.visibility', 0)
cmds.setKeyframe('bubble')
bubbleRise('bubble')

# create duplicate bubbles
for i in range(1, 20):
    cmds.currentTime(0)
    cmds.duplicate('bubble')
    bubbleName = 'bubble' + str(i)
    x = random.randint(-6, 6)
    z = random.randint(-6, 6)
    cmds.select(bubbleName)
    cmds.move(x, 0, z)
    cmds.setAttr(bubbleName+'.visibility', 0)
    cmds.setKeyframe(bubbleName)
    bubbleRise(bubbleName)
