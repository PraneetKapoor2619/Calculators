'''
25.05.2021
A simple program which prints out the curve of the derivate of a function
'''
import math as m
import numpy as np
import matplotlib.pyplot as plt

step = 0.001
X = np.arange(0, 100, step)

'''
Setting up for input function f(x)
Loop(x <- X)
	y = f(x)
	Y = Y + y (append) operation
'''
Y = np.array([])
for x in X:
	y = m.sin(x)		#Enter the function here. By default it is sin(x)
	Y = np.append(Y, y)

'''
The purpose of the Dflag and the associated conditonal block is to prevent a sudden "jump" in the curve of dy/dx if dy = 0 for i = 0. Also, if we skip the value of i = 0, a mismatch occurs in vectors during plotting which we do not want.
'''
DY = np.array([])
Dflag = 1
for i in range(len(Y)):
	if(i > 0):
		dy = (Y[i] - Y[i - 1]) / step
		if(Dflag == 1):
			Dflag = 0
			DY = np.append(DY, dy)
		DY = np.append(DY, dy)

plt.subplot(2, 1, 1)
plt.plot(X, Y, 'k')
plt.xlabel('x')
plt.ylabel('y = f(x)')
plt.title("Curve of the function")

plt.subplot(2, 1, 2)
plt.plot(X, DY, 'r')
plt.xlabel('x')
plt.ylabel("y = f'(x)")
plt.title("Curve of the derivative of the function")
plt.show()
