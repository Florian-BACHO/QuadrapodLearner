from .leg import Leg, LegType
from .dxl.dxlchain import DxlChain
import logging
from settings import *

class QuadrapodMotors:
    def __init__(self, path):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
        self.chain = DxlChain(path, rate=1000000)
        self.chain.get_motor_list()
        self.legs = [
            Leg(LegType.FRONT_RIGHT, frontRightIds, self.chain),
            Leg(LegType.FRONT_LEFT, frontLeftIds, self.chain),
            Leg(LegType.BACK_LEFT, backLeftIds, self.chain),
            Leg(LegType.BACK_RIGHT, backRightIds, self.chain)
        ]

    def setGlobalSpeed(self, value):
        ids = self.chain.get_motors()
        for id in ids:
            self.chain.set_reg(id, "moving_speed", value)

    def waitStopped(self):
        try:
            self.chain.wait_stopped()
        except:
            return

    def setGlobalTorque(self, value):
        ids = self.chain.get_motors()
        for id in ids:
            self.chain.set_reg(id, "max_torque", value)
            self.chain.set_reg(id, "torque_limit", value)

    def getLeg(self, legType):
        for leg in self.legs:
            if leg.legType == legType:
                return leg
        raise RuntimeError("Cannot find leg: {}".format(legType))

    def getAllMotors(self):
        out = []
        for leg in self.legs:
            for it in leg.joints:
                out.append(it)
        return (out)

    def __str__(self):
        res = "Hexapod, {} legs:".format(len(self.legs))
        for leg in self.legs:
            res += '\n\t' + str(leg)
        return res
