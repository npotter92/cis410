"""
bubble.py
Script to animate one bubble rising.
Author: Nate Potter
"""

from nimble import cmds
import random

cmds.currentTime(0)
r = random.randint(1, 10) / 20
c = cmds.polySphere(name="bubble", radius=r)[0]

cmds.scale(1, 0.32, 1)
cmds.setKeyframe("bubble")

cmds.currentTime(24)
cmds.move(0.25, 0.9, -0.25, relative=True)
cmds.scale(1, 0.55, 1)
cmds.setKeyframe("bubble")

cmds.currentTime(48)
cmds.move(-0.75, 4.2, 0.75, relative=True)
cmds.scale(1, 0.8, 1)
cmds.setKeyframe("bubble")

cmds.currentTime(72)
cmds.move(1, 8, -1, relative=True)
cmds.scale(1, 1, 1)
cmds.setKeyframe("bubble")