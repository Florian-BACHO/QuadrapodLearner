from math import sqrt
from math import fabs
from random import randint
from math import pow
import numpy as np
from settings import *
from positionInitializer import getInitialMotorsPositions
import time

class GetUpEnvironment:
    def __init__(self, qMotors, myAHRS, distSensor1, distSensor2):
        self.qMotors = qMotors
        self.allMotors = qMotors.getAllMotors()
        self.myAHRS = myAHRS
        self.distSensor1 = distSensor1
        self.distSensor2 = distSensor2
        self.initMotorBounds()
        self.step = 0
        self.begin = time.time()

    def initMotorBounds(self):
        self.motorsBounds = []
        for i, it in enumerate(getInitialMotorsPositions()):
            if motorsDirs[i] == -1:
                self.motorsBounds.append([it - maxMotorStep, it])
            elif motorsDirs[i] == 1:
                self.motorsBounds.append([it, it + maxMotorStep])

    def getObs(self):
        out = [(it.getPosition() - self.motorsBounds[i][0]) / (self.motorsBounds[i][1] - self.motorsBounds[i][0]) \
               for i, it in enumerate(self.allMotors)]
        return np.array(out)

    def waitEndOfActions(self):
        self.qMotors.waitStopped()

    def reset(self):
        self.step = 0
        for i, it in enumerate(self.allMotors):
            randPos = randint(0, nbMove - 1)
            pos = self.motorsBounds[i][0] + (moveStepSize * randPos)
            it.goto(pos)
        self.waitEndOfActions()
        self.begin = time.time()
        return self.getObs()

    def executeStep(self, action):
        reward = 0.
        done = False

        if time.time() - self.begin >= maxTryDuration:
            done = True

        motor = int(action / nbActionPerMotor)
        action = action % nbActionPerMotor

        if motor < nbMotor:
            pos = self.allMotors[motor].getPosition()
            if action == 0:
                pos += moveStepSize
            elif action == 1:
                pos -= moveStepSize
            if pos < self.motorsBounds[motor][0]:
                pos = self.motorsBounds[motor][0]
            elif pos > self.motorsBounds[motor][1]:
                pos = self.motorsBounds[motor][1]
            self.allMotors[motor].goto(pos)

        reward -= fabs(17 - self.distSensor1.getDistance())
        reward -= fabs(17 - self.distSensor2.getDistance())
        data = self.myAHRS.getValues()
        reward -= fabs(data[1] * gyroRewardCoeff)
        reward -= fabs(data[2] * gyroRewardCoeff)

        self.step += 1

        obs = self.getObs()
        return obs, reward, done
