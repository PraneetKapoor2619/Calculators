import cmath as cm
import numpy as np
import re
import timeit

def seq_generator() :
	seq = input("Enter the input sequence (elements separated by commas): ")
	start = timeit.default_timer()
	extr = re.findall('[0-9ij\+\-.]+', seq)

	X = list()
	check = 0
	for i in range(len(extr)):
		if (extr[i] == '+' or extr[i] == '-') :
			X.append(complex(extr[i - 1] + extr[i] + extr[i + 1]))
			check = 1
		else :
			if check == 1:
				check = 0
			else :
				try :
					if (extr[i + 1] != '+' and extr[i + 1] != '-') :
						xXappend(complex(extr[i]))
				except :
					X.append(complex(extr[i]))
	return X

if __name__ == "__main__" :
	print("x1(n)")
	x1 = np.array(seq_generator())
	print("x2(n)")
	x2 = np.array(seq_generator())
	print(x1, "\n", x2)
	diff = x1.size - x2.size
	if diff < 0 : x1 = np.append(x1, np.zeros(-1 * diff))
	elif diff > 0 : x2 = np.append(x2, np.zeros(diff))
	print("Zero padding done\nx1(n)\n", x1, "\nx2(n)\n", x2, "\n")
	N = x1.size
	yn = np.array([])
	X2_n = np.zeros((N,)*2)
	for m in range(N) :
		x2_col = np.array([])
		for n in range(N) :
			if n - m >= 0 :
				x2_col = np.append(x2_col, x2[n - m])
			else :
				x2_col = np.append(x2_col, x2[N + n - m])
		X2_n[m] = x2_col
	X2_n = X2_n.T
	yn = np.dot(X2_n, x1)
	print("\n\nyn\n", yn)