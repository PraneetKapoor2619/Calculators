import numpy as np
import matplotlib.pyplot as plt
import math

x_axis = np.array([])
y_axis = np.array([])

mid = (1059 + 640) / 2 
initial_error = 1059 - mid
for t in np.arange(1059, 630, -1) :
	error = t - mid
	x_axis = np.append(x_axis, error)
	func = 35 * math.tan(((45 * 3.142)/180) * (error/initial_error))
	y_axis = np.append(y_axis, func)
plt.figure()
plt.plot(x_axis, y_axis, color = 'k')
plt.xlabel('Distance (Pixels)')
plt.ylabel('Angle (radians)')
plt.show()
plt.close()
