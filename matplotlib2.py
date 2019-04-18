
import numpy as np
import matplotlib.pyplot as plt


def curve(x):
    value = (x-0.2)*4.0
    return np.clip(value, 0, 1)

x = np.arange(0, 1, 0.001)
y = curve(x)
print 1
plt.plot(x, y)
print 2
plt.show()
print 3


'''
import math
array = [0.0, 0.6, 0.6, 0.6, 0.6]
gray = array[0]
weight = 0
for i in range (1, 5):
    other_gray = array[i];
    theta = 0.1313*gray-0.0008;
    x = (other_gray-gray)*(other_gray-gray)/theta/theta;
    print x
    weight = 0.368*math.exp(-x);
    print weight
    '''
