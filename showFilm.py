import cv
import sys
capture = cv.CreateCameraCapture( 0 );
cv.NamedWindow( "Fig", 1);
frame = cv.QueryFrame( capture );
S1, S2 = cv.GetSize( frame );
while True:
	frame = cv.QueryFrame( capture );
	if not frame:
		cv.WaitKey( 0 )
		break;
	cv.ShowImage("Fig",frame);
	c = cv.WaitKey(10);
	if c == 27: break
