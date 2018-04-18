#!/usr/bin/python3
from quadrapodMotors.quadrapodMotors import QuadrapodMotors
from quadrapodMotors.leg import LegType
from quadrapodMotors.joint import JointType
from settings import *

def saveInitialMotorsPositions(motorList):
    file = open(initialPosFilename, "w")
    for it in motorList:
        file.write(str(it.getPosition()) + "\n")
    file.close()

def getInitialMotorsPositions():
    out = []
    file = open(initialPosFilename, "r")
    for line in file.readlines():
        if line != "":
            out.append(float(line))
    file.close()
    return (out)

if __name__ == "__main__":
    qMotors = QuadrapodMotors("/dev/ttyACM1")
    motors = qMotors.getAllMotors()
    saveInitialMotorsPositions(motors)
