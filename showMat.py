import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

if len(sys.argv) > 1:
	fname = sys.argv[1]
	a = np.loadtxt(fname)
	plt.imshow(a)
	plt.show()
