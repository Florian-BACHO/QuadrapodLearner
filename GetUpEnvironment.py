from math import sqrt
import numpy as np
from settings import *

class GetUpEnvironment:
    def __init__(self):
        self.reset()

    def getObs(self):
        return np.array([i for i in range(nbMotor)])

    def reset(self):
        self.step = 0
        return self.getObs()

    def executeStep(self, action):
        obs = self.getObs()
        reward = 1.
        done = False

        if self.step >= maxStep:
            done = True
        self.step += 1

        return obs, reward, done
