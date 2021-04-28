import numpy as np
diff1=[]
diff2=[]
diff3=[]
bias1=[]
bias2=[]
bias3=[]
diff1 = np.zeros(shape=(512))
bias1 = np.zeros(shape=(512))
array=np.random.normal(0, 0.015, 3300)
print(array)
import matplotlib.pyplot as plt
np.save('fluctuation30_1mV.npy',array)
plt.hist(array, bins=50, color='steelblue', density=True )
plt.show()
output_file = open("bu40n3.mdl", "w")
header_file = open("bu40n2.mdl","r")
line = header_file.readline()
for line in  header_file.readlines()[0:51]:
        output_file.write(line)

for i in  range(3200):
    output_file.write("******************* 1.8V NMOS%d *************************\n" %(i+2))
    output_file.write(".MODEL N%d.1 NMOS\n" %(i+2))


    header_file = open("bu40n2.mdl", "r")
    line = header_file.readline()
    for line in  header_file.readlines()[53:66]:
            output_file.write(line)

    if array[i]>=0:
        output_file.write("+ VTH0 = 'delvtn + 0.4624 + %s '\n" %(array[i]))
    if array[i]<0:
        output_file.write("+ VTH0 = 'delvtn + 0.4624 %s '\n" % (array[i]))

    header_file = open("bu40n2.mdl", "r")
    line = header_file.readline()
    for line in  header_file.readlines()[67:352]:
        output_file.write(line)


    output_file.write("\n")


output_file.close()
#print(array)