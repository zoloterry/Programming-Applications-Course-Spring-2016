#import numpy and matlibplots module
import math
import numpy as np
import matplotlib.pyplot as plt

#generate array of x values from 0 to 6pi
xValue = np.linspace(0, 6*math.pi)

#calculate y values for sin wave
ySin = np.sin(xValue)

#calculate y values for cosine wave
yCos = np.cos(xValue)

#plot x and y values for both functions 
plt.show()

#set dashed line for sine wave and solide line for cosine wave
plt.plot(xValue, ySin, '--', label = 'Sine Wave')
plt.plot(xValue, yCos, '-', label = 'Cosine Wave')

#add legend
plt.legend()

#leave comment here with your information
#Name:Alphonzo St. Fleur
#Date:01/18/2016

