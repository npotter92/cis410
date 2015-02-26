__author__ = 'Nate'

import math

class Flock:

    def __init__(self, _alignmentWeight, _cohesionWeight, _separationWeight, _speed, _distance):
        self.flockers = []
        self.alignmentWeight = _alignmentWeight
        self.cohesionWeight = _cohesionWeight
        self.separationWeight = _separationWeight
        self.speed = _speed
        self.distance = _distance

    def addFlocker(self, xPos, yPos, zPos, xVel, yVel, zVel, name):
        self.flockers.append(Flocker3D(xPos, yPos, zPos, xVel, yVel, zVel, name))

    def getFlocker(self, index):
        return self.flockers[index]

    def setAlignment(self, weight):
        self.alignmentWeight = weight

    def setCohesion(self, weight):
        self.cohesionWeight = weight

    def setSeparation(self, weight):
        self.separationWeight = weight

class Flocker3D:

    """
    Class for members of the flock

    Attributes:
        xPos - the position on the x axis of the flocker
        yPos - the position on the y axis of the flocker
        zPos - the position on the z axis of the flocker
        xVel - the velocity of the flocker in the x direction
        yVel - the velocity of the flocker in the y direction
        zVel - the velocity of the flocker in the z direction
        name - the string for the name of the flocker
    """

    def __init__(self, _xPos, _yPos, _zPos, _xVel, _yVel, _zVel, _name):
        self.xPos = _xPos
        self.yPos = _yPos
        self.zPos = _zPos
        self.xVel = _xVel
        self.yVel = _yVel
        self.zVel = _zVel
        self.name = _name

    def updatePostion(self):
        """
        Updates the position of the flocker based on its velocity
        :return: Nothing
        """
        self.xPos += self.xVel
        self.yPos += self.yVel
        self.zPos += self.zVel

    def updateVelocity(self, flock):
        """
        Updates the velocity of the flocker based on the algorithms of alignment, cohesion and separation
        :return: Nothing
        """
        alignment = self.computeAlignment(flock)
        cohesion = self.computeCohesion(flock)
        separation = self.computeSeparation(flock)

        self.xVel += alignment[0] * flock.alignmentWeight + cohesion[0] * flock.cohesionWeight + separation[0] * flock.separationWeight
        self.yVel += alignment[1] * flock.alignmentWeight + cohesion[1] * flock.cohesionWeight + separation[1] * flock.separationWeight
        self.zVel += alignment[2] * flock.alignmentWeight + cohesion[2] * flock.cohesionWeight + separation[2] * flock.separationWeight

        if self.xPos >= 10:
            self.xVel = -math.fabs(self.xVel)
        if self.xPos <= -10:
            self.xVel = math.fabs(self.xVel)
        if self.yPos >= 10:
            self.yVel = -math.fabs(self.yVel)
        if self.yPos <= -10:
            self.yVel = math.fabs(self.yVel)
        if self.zPos >= 10:
            self.zVel = -math.fabs(self.zVel)
        if self.zPos <= -10:
            self.zVel = math.fabs(self.zVel)

        # normalize the vector
        length = math.sqrt((self.xVel * self.xVel) + (self.yVel * self.yVel) + (self.zVel * self.zVel))
        self.xVel /= length
        self.yVel /= length
        self.zVel /= length
        self.xVel *= flock.speed
        self.yVel *= flock.speed
        self.zVel *= flock.speed

    def distanceFrom(self, other):
        """
        Computes the distance between two flockers
        :param other: other flocker
        :return: distance between self and other
        """
        distance = math.sqrt((self.xPos - other.xPos) ** 2 + (self.yPos - other.yPos) ** 2 + (self.zPos - other.zPos) ** 2)
        return distance

    def computeAlignment(self, flock):
        """
        Compute a vector whose velocity aligns with that of neighboring flockers
        :return: vector v
        """

        v = [0, 0, 0]
        numNeighbors = 0

        for other in flock.flockers:
            if other != self:
                if self.distanceFrom(other) < flock.distance:
                    v[0] += other.xVel
                    v[1] += other.yVel
                    v[2] += other.zVel
                    numNeighbors += 1

        if numNeighbors == 0:
            return v

        v[0] /= numNeighbors
        v[1] /= numNeighbors
        v[2] /= numNeighbors
        # normalize the vector
        length = math.sqrt((v[0] * v[0]) + (v[1] * v[1]) + (v[2] * v[2]))
        if length == 0:
            return v
        v[0] /= length
        v[1] /= length
        v[2] /= length

        return v

    def computeCohesion(self, flock):
        """
        Compute a vector that points towards the center of mass of neighboring flockers
        :return: vector v
        """

        v = [0, 0, 0]
        numNeighbors = 0

        for other in flock.flockers:
            if other != self:
                if self.distanceFrom(other) < flock.distance:
                    v[0] += other.xPos
                    v[1] += other.yPos
                    v[2] += other.zPos
                    numNeighbors += 1

        if numNeighbors == 0:
            return v

        v[0] /= numNeighbors
        v[1] /= numNeighbors
        v[2] /= numNeighbors
        v[0] -= self.xPos
        v[1] -= self.yPos
        v[2] -= self.zPos

        # normalize the vector
        length = math.sqrt((v[0] * v[0]) + (v[1] * v[1]) + (v[2] * v[2]))
        if length == 0:
            return v
        v[0] /= length
        v[1] /= length
        v[2] /= length

        return v

    def computeSeparation(self, flock):
        """
        Compute a vector that points away from neighboring flockers
        :return: vector v
        """

        v = [0, 0, 0]
        numNeighbors = 0

        for other in flock.flockers:
            if other != self:
                if self.distanceFrom(other) < flock.distance:
                    v[0] += other.xPos - self.xPos
                    v[1] += other.yPos - self.yPos
                    v[2] += other.zPos - self.zPos
                    numNeighbors += 1

        if numNeighbors == 0:
            return v

        v[0] /= numNeighbors
        v[1] /= numNeighbors
        v[2] /= numNeighbors
        v[0] *= -1
        v[1] *= -1
        v[2] *= -1

        # normalize the vector
        length = math.sqrt((v[0] * v[0]) + (v[1] * v[1]) + (v[2] * v[2]))
        if length == 0:
            return v
        v[0] /= length
        v[1] /= length
        v[2] /= length

        return v