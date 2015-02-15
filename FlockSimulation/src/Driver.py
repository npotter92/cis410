__author__ = 'Nate'

from nimble import cmds
import random
from Flocker import Flocker


# Create the flock
f0 = Flocker(random.randint(-6, 6), random.randint(0, 12), random.randint(-6, 6), .1, .1, .3, "f0")
cmds.polySphere(name=f0.name, radius=0.2)

f1 = Flocker(random.randint(-6, 6), random.randint(0, 12), random.randint(-6, 6), .2, .3, .1, "f1")
cmds.polySphere(name=f1.name, radius=0.2)

f2 = Flocker(random.randint(-6, 6), random.randint(0, 12), random.randint(-6, 6), .2, .3, .1, "f2")
cmds.polySphere(name=f2.name, radius=0.2)

