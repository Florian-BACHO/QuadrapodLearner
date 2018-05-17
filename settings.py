# Reinforcement Learning
#     Environement
nbLeg = 4 # 2 front legs and 2 back legs
nbMotorPerLeg = 3
nbMotor = nbLeg * nbMotorPerLeg
nbActionPerMotor = 3 # Move up ; Wait ; Move down
maxStep = 100 # Maximum step in a try
nbAction = 3 # Buy, Wait, Sell
punishLosses = True
punishCoeff = 1.0
discountRate = 0.5

#     Learning Parameters
nbTrain = 500 # Maximum train epoch
nbTryPerTrain = 10 # Number of try each epoch

# Neural network
nbHistory = 20 # Number of historical data given to the recurrent layer
nbEntry = nbMotor
nbHiddens = [50]
nbOutput = nbAction # Argmax on linear output
modelSavePath = "./trainSave/model.ckpt"
#     Gradient Descent Parameters
learningRate = 1e-2
