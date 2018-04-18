from math import fabs
import tensorflow as tf
import numpy as np
from GetUpEnvironment import *
from os import path
import random
from settings import *
from motorsANN import *

class GetUp:
    def __init__(self, qMotors, myAHRS, distSensor1, distSensor2):
        self.env = GetUpEnvironment(qMotors, myAHRS, distSensor1, distSensor2)
        self.ann = MotorsANN()

        self.iteration = tf.Variable(0)
        self.incrementIteration = tf.assign(self.iteration, self.iteration + 1)

        self.init = tf.global_variables_initializer() # Variable initializer

    # Execute the discount operation on rewards
    def discountRewards(self, rewards):
        out = []
        cumul = 0
        for i in reversed(range(len(rewards))):
            cumul = rewards[i] + (cumul * discountRate)
            out.insert(0, cumul)
        return out

    # Discount all rewards and normalize them
    def discountAndNormalizeRewards(self, all_rewards):
        # Discount for each try
        discounted_rewards = [self.discountRewards(rewards) for rewards in all_rewards]
        flat = np.concatenate(discounted_rewards) # Concatenate all discounted rewards in a single list
        mean = flat.mean() # Mean
        std = flat.std() # Standard deviation
        return [(rewards - mean) / (std + 1e-10) for rewards in discounted_rewards] # Return normalized discounted rewards

    def executeLearningPeriod(self, session):
        session.run(self.incrementIteration)
        print("Iteration %d" % self.iteration.eval())
        all_rewards = [] # Rewards of all tries in the train iteration

        for try_number in range(nbTryPerTrain):
            # Run a try
            obs = self.env.reset() # Reset environment & get first observation
            current_rewards = [] # Rewards of current try

            while True:
                a = self.ann.takeLearningAction(session, obs) # Take a decision

                obs, reward, done = self.env.executeStep(a) # Execute the action in the environment
                current_rewards.append(reward)

                if done: # Break if the try is finished
                    break
            print(reward)
            all_rewards.append(current_rewards)
            self.ann.newTry()

        all_rewards = self.discountAndNormalizeRewards(all_rewards)
        self.ann.applyGradients(session, all_rewards)

    def execute(self, session):
        obs = self.env.reset()
        rewards = []
        while True:
            a = self.ann.takeAction(session, obs)
            obs, reward, done = self.env.executeStep(a)
            rewards.append(reward)
            if done:
                break

        print(rewards)
