import time
import numpy as np

acc = 0
with open("yada.txt", 'w+') as f:
    for i in range(10000):
        now = time.time()
        f.write("yaga,")
        acc += time.time()-now
print("\nopen text file and write:\n", acc)


acc = 0
yeet = []
for i in range(10000):
    now = time.time()
    yeet.append("yaga")
    acc += time.time()-now
print("\nappend to python list:\n", acc)

acc = 0
yeet2 = ["0"]*10000
for i in range(10000):
    now = time.time()
    yeet2[i] = "yaga,"
    acc += time.time()-now
print("\nset elem of prealloc'd python list:\n", acc)

acc = 0
yeet3 = np.array(["     " for i in range(10000)])
for i in range(10000):
    now = time.time()
    yeet3[i] = "yaga,"
    acc += time.time()-now
print("\nset elem of prealloc'd numpy array:\n", acc)
