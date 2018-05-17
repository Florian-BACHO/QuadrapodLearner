from math import fabs
import tensorflow as tf
import numpy as np
from GetUpEnvironment import *
from os import path
import random
import settings


class GetUp:
    def __init__(self):
        self.env = GetUpEnvironment()

        self.createANN()
        self.initLearning()

        self.init = tf.global_variables_initializer() # Variable initializer
        #self.saver = tf.train.Saver()

    def createANN(self):
        # Construct neural network
        self.entry = tf.placeholder(tf.float32, shape=[None, nbEntry], name="entry")
        self.hiddens = []
        for i, it in enumerate(nbHiddens):
            self.hiddens.append(tf.layers.dense(self.entry if i == 0 else \
                                                self.hiddens[-1], it, activation=tf.nn.selu))
        # One output layer per motor
        self.out = tf.concat([tf.layers.dense(self.hiddens[-1], nbActionPerMotor) for _ in range(nbMotor)], axis=0)
        # Actions taken randomly with output layers probabilities
        self.actionsLearning = tf.transpose(tf.multinomial(tf.log(tf.nn.softmax(self.out)), num_samples=1))
        # Taken actions are outputs argmax
        self.actions = tf.argmax(self.out, axis=1)

    def initLearning(self):
        self.y = tf.placeholder(tf.int32, shape=[nbMotor]) # Expected activations
        self.xentropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=self.out, labels=self.y) # Loss

        self.optimizer = tf.train.AdamOptimizer(learning_rate=learningRate)
        self.grad_and_vars = self.optimizer.compute_gradients(self.xentropy) # Compute gradients
        self.gradients = [grad for grad, var in self.grad_and_vars] # Get gradients
        self.initGradientPlaceholders()
        self.training_op = self.optimizer.apply_gradients(self.grad_and_vars_feed)

        self.iteration = tf.Variable(0)
        self.incrementIteration = tf.assign(self.iteration, self.iteration + 1)

    def initGradientPlaceholders(self):
        self.gradient_placeholders = [] # Array of placeholders for gradients
        self.grad_and_vars_feed = [] # Array that will feed the optimizer with computed gradients
        for grad, var in self.grad_and_vars:
            tmp_placeholder = tf.placeholder(tf.float32, shape=grad.get_shape())
            self.gradient_placeholders.append(tmp_placeholder)
            self.grad_and_vars_feed.append((tmp_placeholder, var))

    # Feed dictionary to give to the optimizer
    def getGradientFeed(self, gradients, all_rewards):
        feed_dict = {}
        for grad_idx, grad_placeholder in enumerate(self.gradient_placeholders):
            tmp_grad = [] # Gradient * Reward
            for try_index, rewards in enumerate(all_rewards): # For each try
                for step, reward in enumerate(rewards): # For each step in current try
                    tmp_grad.append(reward * gradients[try_index][step][grad_idx]) # Gradient * reward
            mean_gradients = np.mean(tmp_grad, axis=0) # Mean gradients
            feed_dict[grad_placeholder] = mean_gradients
        return feed_dict

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
        return [(rewards - mean) / std for rewards in discounted_rewards] # Return normalized discounted rewards

    def executePeriod(self, session):
        session.run(self.incrementIteration)
        print("Iteration %d" % self.iteration.eval())
        all_rewards = [] # Rewards of all tries in the train iteration
        all_gradients = [] # Gradients of all tries in the train iteration

        for try_number in range(nbTryPerTrain):
            # Run a try
            obs = self.env.reset() # Reset environment & get first observation

            current_rewards = [] # Rewards of current try
            current_gradients = [] # Gradients of current try

            for i in range(maxStep + 1):
                a = self.actionsLearning.eval(feed_dict={self.entry: [obs]})[0] # Take a decision
                grads = session.run(self.gradients, feed_dict={self.entry: [obs], self.y: a}) # Get gradients

                obs, reward, done = self.env.executeStep(a) # Execute the action in the environment
                current_rewards.append(reward)
                current_gradients.append(grads)

                if done: # Break if the try is finished
                    break;
            print(obs, reward)
            all_rewards.append(current_rewards)
            all_gradients.append(current_gradients)

        all_rewards = self.discountAndNormalizeRewards(all_rewards)
        # Compute policy gradients with rewards
        feed_dict = self.getGradientFeed(all_gradients, all_rewards)
        # Execute policy gradient descent
        session.run(self.training_op, feed_dict=feed_dict)
        #save_path = self.saver.save(session, modelSavePath)

    def getAction(self, session, obs):
        return self.actions.eval(feed_dict={entry: [obs]}) # Take a decision
