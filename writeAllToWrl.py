import numpy as np
import cv,cv2
import os
import matplotlib.pyplot as plt
from amircv.amtools import amimtools
from amircv.amtools import amplottools

root = '/Users/amirrahimi/Desktop/doc/visionTools/lasik-2.4/amir/SavedPics/Make3D/bld_smooth/stop_1e-3/bld_center_gnd/'

images_paths = os.listdir(root)
for image_name in images_paths:
	img = cv2.imread(root+image_name)
	img = img[:,:,::-1]
	img_float = np.float32(img)
	img_float /= 255.
	img_float *= 80.
	img_float[0][0] = img_float[1][0] = img_float[1][1]
	d = img_float[:,:,0]
	orig_name = image_name[0:image_name.find('_')] +'-resized.jpg'
	print orig_name
	orig_img = cv2.imread('/Users/amirrahimi/Downloads/Applications/cvpr10Data/images/'+orig_name)
	orig_img = orig_img[:,:,::-1]
	amplottools.writeToVRMLFacesNoZero(d,orig_img,'output/'+orig_name + '.wrl')

