#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import cv, cv2
import sys

imgRoot = '/Users/amirrahimi/temp/opencv/allSegment/TehranPics/'

str = 'img-combined1-p-108t0_vpmap_segm.png'
if len(sys.argv) == 2:
	str = sys.argv[1]
base = str[:-15]
imgName = imgRoot + base +'.jpg'

if str[0] == 'I':
	imgRoot = '/Users/amirrahimi/temp/opencv/allSegment/segmentToLabel/Ny320x240/'
	imgName = imgRoot + base + '.jpg'

	
if str[0] == 'i':
	imgRoot = '/Users/amirrahimi/Downloads/Applications/cvpr10Data/images/'
	imgName = imgRoot + base + '-resized.jpg'

#'/Users/amirrahimi/temp/opencv/allSegment/mixedImages/'
print imgName
img = cv2.imread(imgName)
print img.shape
img = img[:,:,::-1]
a = cv2.imread(str)
b = a.ravel()
print b.shape
idx3 = np.where( b == 3)
print 'len(idx3) : ',len(idx3[0])
idx2 = np.where( b == 2)
idx1 = np.where( b == 1)
print 'len(idx2) : ',len(idx2[0])
print 'len(idx1) : ',len(idx1[0])
b = img.ravel()
print b.shape
#b[idx3] = 0
#b[idx3[0][2::3]] = 255
if len(idx3[0]) > 0:
	b[idx2] = 0
	b[idx2[0][1::3]] = 255
if len(idx2[0]) > 0:
	b[idx1] = 0
	b[idx1[0][0::3]] = 255
c=b.reshape(a.shape)
plt.axis('off')
plt.imshow(c)
plt.show()
