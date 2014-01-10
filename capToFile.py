import cv2
import numpy as np

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
writer = cv2.VideoWriter(filename="file.avi", 
		fourcc=cv2.cv.CV_FOURCC('X', 'V', 'I', 'D'), #this is the codec that works for me
		fps=15, #frames per second, I suggest 15 as a rough initial estimate
		frameSize=(640, 480))
if vc.isOpened(): # try to get the first frame
	rval, frame = vc.read()
	print frame.shape
else:
	rval = False

while rval:
	cv2.imshow("preview", frame)
	rval, frame = vc.read()
	writer.write(frame)
	key = cv2.waitKey(20)
	if key == 27: # exit on ESC
		break
