# Reinforcement Learning

#       Environement
maxTryDuration = 4.0 # Maximum duration in a try
nbTrain = 500 # Maximum train epoch
nbTryPerTrain = 10 # Number of try each epoch
punishLosses = True
punishCoeff = 1.0
discountRate = 0.5
gyroRewardCoeff = 0.5

#       Quadrapod properties
nbLeg = 4 # 2 front legs and 2 back legs
nbMotorPerLeg = 3
nbMotor = nbLeg * nbMotorPerLeg
nbActionPerMotor = 3 # Move up ; Wait ; Move down
maxMotorAngle = 90 # Limit motors to 90 degree angle
nbMove = 5 # Number of step that the quadrapod have to execute to reach 90 degree
frontRightDirs = [-1., 1., -1] # Coxa, femur, tibia
frontLeftDirs = [1., 1., -1]
backRightDirs = [1., 1., -1]
backLeftDirs = [-1., 1., -1]
motorsDirs = frontRightDirs + frontLeftDirs + backLeftDirs + backRightDirs
initialPosFilename = "motorPos.conf"

#       Motors
#               Physical Properties
frontRightIds = [10, 11, 12] # Coxa, femur, tibia
frontLeftIds = [20, 21, 22]
backLeftIds = [30, 31, 32]
backRightIds = [40, 41, 42]
motorAngle = 300 # From 0 to 300 degree
nbMotorStep = 1024 # Possibles positions
motorSpeed = 1023
motorTorque = 800

#       Properties for the quadrapod (limits)
maxMotorStep = (nbMotorStep * maxMotorAngle) / motorAngle # Number of step with 90 angle
moveStepSize = maxMotorStep / nbMove

#       Neural network
nbEntry = nbMotor
nbHiddens = [30, 50, 30]
nbOutput = nbActionPerMotor * nbMotor # Argmax on linear output
modelSavePath = "./trainSave/model.ckpt"
learningRate = 1e-2
