#!/usr/bin/python3
from getUp import *
from quadrapodMotors.quadrapodMotors import QuadrapodMotors
from quadrapodMotors.leg import LegType
from quadrapodMotors.joint import JointType
from myAHRS_plus import *
from DistanceSensor import *

def main():
    qMotors = QuadrapodMotors("/dev/ttyACM1")
    qMotors.setGlobalSpeed(motorSpeed)
    qMotors.setGlobalTorque(motorTorque)

    myAHRS = myAHRS_plus("/dev/ttyACM0")
    distSensor1 = DistanceSensor(8, 7)
    distSensor2 = DistanceSensor(23, 24)

    getUpModel = GetUp(qMotors, myAHRS, distSensor1, distSensor2)

    init = tf.global_variables_initializer()
    saver = tf.train.Saver()

    # Run the session
    with tf.Session() as sess:
        sess.run(init) # Initialize variables

        if path.exists(modelSavePath + ".meta"):
            saver.restore(sess, modelSavePath)
        while True:
            getUpModel.executeLearningPeriod(sess)
            save_path = saver.save(sess, modelSavePath)

if __name__ == "__main__":
    print("=== Quadrapod Learner ===")
    main()
