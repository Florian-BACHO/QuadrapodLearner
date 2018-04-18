from enum import Enum
from .joint import Joint, JointType

class Leg:
    def __init__(self, legType, servoIds, chain):
        assert len(servoIds) == 3
        self.chain = chain
        self.legType = legType
        self.joints = [
            Joint(JointType.COXA, servoIds[0], self.chain),
            Joint(JointType.FEMUR, servoIds[1], self.chain),
            Joint(JointType.TIBIA, servoIds[2], self.chain),
        ]

    def getJoint(self, jointType):
        for joint in self.joints:
            if joint.jointType == jointType:
                return joint
        raise RuntimeError("Cannot find joint: {}".format(jointType))

    def __str__(self):
        res = "Leg, Id:{}, {} joints:".format(self.legType, len(self.joints))
        for joint in self.joints:
            res += '\n\t' + str(joint)
        return res


FRONT_MASK = 1 << 1
BACK_MASK = 1 << 2
RIGHT_MASK = 1 << 3
LEFT_MASK = 1 << 4

class LegType(Enum):
    FRONT_RIGHT = FRONT_MASK | RIGHT_MASK
    FRONT_LEFT = FRONT_MASK | LEFT_MASK
    BACK_LEFT = BACK_MASK | LEFT_MASK
    BACK_RIGHT = BACK_MASK | RIGHT_MASK
