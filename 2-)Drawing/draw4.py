import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype="uint8")
# Text
cv.putText(blank,"Hello World",(100,200),
           cv.FONT_HERSHEY_DUPLEX,1.0,(220,220,220),thickness=2)
cv.imshow("Text",blank)

cv.waitKey(0)