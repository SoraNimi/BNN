import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

y_test_t017 = np.uint8([])
x_test_t017 = np.ones((1, 28, 28), dtype=np.uint8)

for loop in range(1000):
    if y_test[loop] ==9:
        #print(loop)
        y_test_t017 = np.append(y_test_t017, y_test[loop].astype(np.uint8))
        x_test_t017 = np.append(x_test_t017, np.expand_dims(x_test[loop], 0), axis=0)
x_test_t017 = np.delete(x_test_t017, 0, 0)

y_train_t017 = np.uint8([])
x_train_t017 = np.ones((1, 28, 28), dtype=np.uint8)
for loop in range(1000):
    if y_train[loop]==0:
        y_train_t017= np.append(y_train_t017, y_train[loop].astype(np.uint8))
        x_train_t017 = np.append(x_train_t017, np.expand_dims(x_train[loop], 0), axis=0)

x_train_t017 = np.delete(x_train_t017, 0, 0)


#plt.figure(figsize=(10, 10))
#for i in range(100):
#    plt.subplot(1, 1, i+1)


#    plt.xticks([])
#    plt.yticks([])
#    plt.grid(False)
#    plt.imshow(train_images[i], cmap=plt.cm.binary)
#    plt.imshow(x_train_t017[9])
#    plt.xlabel(y_train_t017[9])
#    plt.ylabel(7+1)
#    plt.show()

print(x_train_t017[0])



for a in range (10):
    output_file = open(("img%s.sp")%(a+91),"w")
    #output_file = open("img1.sp","w")
    output_file.write(".PARAM mvdd=1.8\n")
    output_file.write("VVDD VDD 0 DC mvdd\n")
    output_file.write("VVREF VREF 0 DC mvdd\n")
    output_file.write("VVREFB VREFB 0 DC 0\n")
    for i in range(0,28):
        for j in range(0,28):
            output_file.write("vx%s x%s 0 PWL  \n" %((28*i+j),(28*i+j)))
            output_file.write("+	0n		%s\n" % ("mvdd" if x_test_t017[a+50][i][j] >= 1 else 0))
            output_file.write("+	20n		%s\n" % ("mvdd" if x_test_t017[a+50][i][j] >= 1 else 0))
            output_file.write("+	25n	    %s\n" % ("mvdd" if x_test_t017[a+50][i][j] >= 1 else 0))
            output_file.write("+	200n    %s\n" % ("mvdd" if x_test_t017[a+50][i][j] >= 1 else 0))
            output_file.write('\n')


    output_file.write(".END\n")

    output_file.close()


