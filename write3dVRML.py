import cv,cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'cd /Users/amirrahimi/Desktop/doc/visionTools/lasik-2.4/amir/SavedPics/Make3D/bld_smooth/stop_1e-3/bld_center_gnd')
img = cv2.imread('img-060705-17.51.18-p-018t000_abs_0.306359_log_0.318332_base_gnd.png')
img = img[:,:,::-1]
img_float = np.float32(img)
img_float /= 255.
img_float *= 80.
img_float[0][0] = img_float[1][0] = img_float[1][1]
get_ipython().magic(u'cd ~/temp/python/learningcomputervision/')
get_ipython().magic(u'cd Amir')
from amircv.amtools import amimtools
from amircv.amtools import amplottools
orig_img = cv2.imread('/Users/amirrahimi/Downloads/Applications/cvpr10Data/images/img-060705-17.51.18-p-018t000-resized.jpg')
d = img_float[:,:,0]
amplottools.writeToVRMLFaces(d, orig_img,'dd.wrl')
