import sys

import numpy as np
import matplotlib.pyplot as plt

#import numpy as np 
#from pylab import * 

x=[]
y = []

for line in sys.stdin:
    y = line.Split(" ")
    for i in range(len(y)):
        x.append(i)
        y[i] = float(y[i])

        plt.plot(x,y)
        plt.show()

        plt.bar(x,y)
        plt.show()
        x,y=[]