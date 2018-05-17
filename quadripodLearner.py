#!/usr/bin/python3

from getUp import *

def main():
    getUpModel = GetUp()

    init = tf.global_variables_initializer()
    saver = tf.train.Saver()

    # Run the session
    with tf.Session() as sess:
        sess.run(init) # Initialize variables

        if path.exists(modelSavePath + ".meta"):
            saver.restore(sess, modelSavePath)
        getUpModel.executePeriod(sess)
        save_path = saver.save(sess, modelSavePath)

if __name__ == "__main__":
    main()
