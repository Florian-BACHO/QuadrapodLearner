from math import sqrt
from math import fabs
from random import randint
from math import pow
import numpy as np
from settings import *

class GetUpEnvironment:
    def __init__(self):
        self.reset()

    def getObs(self):
        return np.array(self.motors)

    def reset(self):
        self.step = 0
        self.motors = [randint(-10, 10) for _ in range(nbMotor)]
        return self.getObs()

    def executeStep(self, action):
        reward = 0.
        done = False

        for i, action in enumerate(action):
            if action == 0:
                self.motors[i] -= 1
            elif action == 2:
                self.motors[i] += 1
            if self.motors[i] < -10:
                self.motors[i] = -10
            elif self.motors[i] > 10:
                self.motors[i] = 10

        if self.step >= maxStep:
            done = True

        for it in self.motors:
            reward += pow(10. - fabs(it), 2)

        self.step += 1

        obs = self.getObs()
        return obs, reward, done
