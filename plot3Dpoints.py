#!/usr/bin/env python

import matplotlib.image as mpimage
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from numpy import *
import numpy as np
import sys

def plot3DPoints(X, Y, Z, point_type='go'):
        fig = plt.figure()
        ax = fig.gca(projection="3d")

        ax.plot( X, Y, Z, point_type)
        plt.ylabel('y')
        plt.xlabel('x')
#plt.zlabel('z')
        ax.set_zlabel('z')
        plt.show()
def usage():
	print "Usage: python plot3dpoints.py file.txt\n \
		file.txt should contain X Y Z coordintate of points in\n \
		the columns of file"

if __name__ == "__main__":
	if len(sys.argv) == 2:
		data = np.loadtxt(sys.argv[1])
		if data.shape[1] == 3 and data.shape[0] > 0:
			plot3DPoints( data[:,0], data[:,1], data[:,2] )
		else:
			usage()
	else:
		usage()

