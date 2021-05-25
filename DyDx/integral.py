'''
25.05.2021

This is a program which plots the integral of a function
'''

import math as m
import numpy as np
import matplotlib.pyplot as plt

step = 0.01
X = np.arange(0, 100, step)

Y = np.array([])
for x in X:
	y = m.sin(x)
	Y = np.append(Y, y)

I = np.array([])
i = 0
for y in Y:
	i = i + (step * y)
	I = np.append(I, i)

plt.subplot(2, 1, 1)
plt.plot(X, Y, 'k')
plt.xlabel('x')
plt.ylabel('y = f(x)')
plt.title('Curve of the function')

plt.subplot(2, 1, 2)
plt.plot(X, I, 'r')
plt.xlabel('x')
plt.ylabel('y = integral(f(x))')
plt.title('Curve of integral of the function')

plt.show()
