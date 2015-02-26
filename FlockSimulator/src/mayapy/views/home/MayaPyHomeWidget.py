# MayaPyHomeWidget.py
# (C)2013
# Scott Ernst

from PySide import QtGui

from pyglass.widgets.PyGlassWidget import PyGlassWidget

from mayapy.enum.UserConfigEnum import UserConfigEnum
from mayapy.views.home.NimbleStatusElement import NimbleStatusElement
from mayapy import Driver

#___________________________________________________________________________________________________ MayaPyHomeWidget
class MayaPyHomeWidget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of MayaPyHomeWidget."""
        super(MayaPyHomeWidget, self).__init__(parent, **kwargs)
        self._firstView = True

        self.alignmentWeight = 0
        self.separationWeight = 0
        self.cohesionWeight = 0
        self.numFlockers = 5
        self.speed = 1
        self.numFrames = 120
        self.in3D = False
        self.distance = 5

        weights = ['0', '1', '2', '3', '4', '5']
        numFlockers = ['5', '10', '15', '20', '25', '35', '40', '45', '50']
        speeds = ['1', '2', '3', '4', '5']
        dimensions = ['2D', '3D']
        frames = ['120', '240', '360', '480', '600']
        distances = ['5', '10', '15', '20']

        self.alignmentBox.addItems(weights)
        self.cohesionBox.addItems(weights)
        self.separationBox.addItems(weights)
        self.numFlockersBox.addItems(numFlockers)
        self.speedBox.addItems(speeds)
        self.dimensionsBox.addItems(dimensions)
        self.framesBox.addItems(frames)
        self.distanceBox.addItems(distances)
        self.alignmentBox.setCurrentIndex(0)
        self.cohesionBox.setCurrentIndex(0)
        self.separationBox.setCurrentIndex(0)
        self.numFlockersBox.setCurrentIndex(0)
        self.speedBox.setCurrentIndex(0)
        self.dimensionsBox.setCurrentIndex(0)
        self.framesBox.setCurrentIndex(0)
        self.distanceBox.setCurrentIndex(0)

        self.runButton.clicked.connect(self._run)

        self._statusBox, statusLayout = self._createElementWidget(self, QtGui.QVBoxLayout, True)
        statusLayout.addStretch()

        self._nimbleStatus = NimbleStatusElement(
            self._statusBox,
            disabled=self.mainWindow.appConfig.get(UserConfigEnum.NIMBLE_TEST_STATUS, True) )
        statusLayout.addWidget(self._nimbleStatus)
#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _activateWidgetDisplayImpl
    def _activateWidgetDisplayImpl(self, **kwargs):
        if self._firstView:
            self._nimbleStatus.refresh()
            self._firstView = False

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleAssignment1
    def _run(self):
        self.alignmentWeight = int(self.alignmentBox.currentText())
        self.cohesionWeight = int(self.cohesionBox.currentText())
        self.separationWeight = int(self.separationBox.currentText())
        self.numFlockers = int(self.numFlockersBox.currentText())
        self.speed = int(self.speedBox.currentText())
        self.numFrames = int(self.framesBox.currentText())
        self.distance = int(self.distanceBox.currentText())
        if self.dimensionsBox.currentText() == "2D":
            self.in3D = False
        else:
            self.in3D = True
        Driver.simulate(self.numFlockers,
                        self.numFrames,
                        self.alignmentWeight,
                        self.cohesionWeight,
                        self.separationWeight,
                        self.speed,
                        self.distance,
                        self.in3D)