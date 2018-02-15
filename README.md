# QuadripodLearner
A program that learn how to control a quadripod robot using Deep Reinforcement Learning algorithm (QLearning algorithm using Artificial Neural Network)

- Step 1: Learn how to stand up
- Step 2: Learn how to turn right / left
- Step 3: Learn how to walk
- Step 4: Discover an environment

## Quadripod Details

- NbLegs = 4
- NbMotorPerLegs = 3
- NbMotor = NbLegs * NbMotorPerLegs = 3 * 4 = 12
- Controler: Raspberry Pi 3

### Sensors

- 2 Ultrasonics sensors (HC-SR04): pointing to the ground, it allow us to know the distance from the ground;
- 1 myAHRS+ (Attitude Heading Reference System): his 3-axis 16-bit gyroscope allow us to know the body orientation.

## Artificial Neural Network Details

- Used library: Fast Artificial Neural Network (FANN) C++ Wrapper;
- Number of layer: 3
- Layer 1 (entry layer): nbMotor = 12 neurons;
- Layer 2 (hidden layer): 24 neurons (Sigmoïd activation function);
- Layer 3 (output layer): nbMotor * nbAction = 12 * 3 = 36 (Linear activation function);
- Learning Rate: 0.5.
