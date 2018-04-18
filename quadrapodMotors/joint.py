from enum import Enum
from settings import *
from .dxl.dxlcore import *

class Joint:
    def __init__(self, jointType, servoId, chain):
        self.chain = chain
        self.jointType = jointType
        self.servoId = servoId
        self.lastPos = 0.

    def goto(self, pos, speed=None):
        if pos < 0:
            pos = 0
        if pos > nbMotorStep:
            pos = nbMotorStep - 1
        try:
            self.chain.goto(self.servoId, pos, speed, False)
        except:
            return

    def getPosition(self):
        try:
            pos = self.chain.get_reg(self.servoId, "present_position")
            self.lastPos = pos
            return pos
        except:
            return self.lastPos

    def add(self, toAdd, speed=None):
        self.goto(self.getPosition() + toAdd)

    def __str__(self):
        return "Joint, type:{}, servoId:{}".format(self.jointType, self.servoId)


class JointType(Enum):
    COXA = 0
    FEMUR = 1
    TIBIA = 2
