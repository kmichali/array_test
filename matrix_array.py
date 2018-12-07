import numpy as np
import os

input = np.loadtxt("input.txt", dtype='f', delimiter=',')
print(input)
counter = 0

for i in range(0,input.shape[0]):
    for j in range(0, input.shape[1]):
        counter = counter+1
        print('counter:', counter)
        index = int(os.environ['PBS_ARRAY_INDEX'])
        if counter == index:
            print('processing element', input[i,j])
