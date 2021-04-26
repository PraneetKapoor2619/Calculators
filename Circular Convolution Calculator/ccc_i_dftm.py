import cmath as cm
import numpy as np
import re
import timeit

rnd = 0 

def dft() :
	global rnd
	seq = input("Enter the input sequence (elements separated by commas): ")
	rnd = int(input("Enter the number of places you want to round your answer to: "))
	start = timeit.default_timer()
	extr = re.findall('[0-9ij\+\-.]+', seq)
	print("EXTR: ", extr, "\nCreating the sequence...")

	x = list()
	check = 0
	for i in range(len(extr)):
		if (extr[i] == '+' or extr[i] == '-') :
			x.append(complex(extr[i - 1] + extr[i] + extr[i + 1]))
			check = 1
		else :
			if check == 1:
				check = 0
			else :
				try :
					if (extr[i + 1] != '+' and extr[i + 1] != '-') :
						x.append(complex(extr[i]))
				except :
					x.append(complex(extr[i]))
	print("X: ", x)

	print("Sequence created. Now computing DFT...")
	N = len(x)
	Wn = cm.exp(-1 * 2j * cm.pi / N)
	Xk = list()
	for K in range(len(x)) :
		#print("\n", K)
		sum = 0
		for n in range(len(x)) :
			#print(Wn ** (K * n))
			sum += x[n]*(Wn ** (K * n))
		Xk.append(round(sum.real, rnd) + round(sum.imag, rnd) * 1j)
	stop = timeit.default_timer()
	print("\nTime taken for computations:", stop - start)
	return Xk

def idft(X) :
	global rnd
	start = timeit.default_timer()
	print("Computing IDFT...")
	N = len(X)
	Wn = cm.exp(2j * cm.pi / N)
	x = list()
	for n in range(len(X)) :
		#print("\n", K)
		sum = 0
		for K in range(len(X)) :
			#print(Wn ** (K * n))
			sum += X[K]*(Wn ** (K * n))
		x.append((round(sum.real, rnd) + round(sum.imag, rnd) * 1j)/N)
	stop = timeit.default_timer()
	print("\nTime taken for computations:", stop - start)
	return x
	
if __name__ == "__main__" :
	X1 = np.array(dft())
	X2 = np.array(dft())
	diff = X1.size - X2.size
	if diff < 0 : X1 = np.append(X1, np.zeros(-1 * diff))
	elif diff > 0 : X2 = np.append(X2, np.zeros(diff))
	print("Zero padding done\nX1(n)\n", X1, "\nX2(n)\n", X2, "\n")
	y = idft(X1 * X2)
	print("Circular convolution result is: \n", y)