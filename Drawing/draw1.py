import cv2 as cv
import numpy as np
# np.zeros(width,height,numberOfColorChannel
blank=np.zeros((500,500,3),dtype="uint8") # black image
cv.imshow("Black",blank)

blank[:]=0,255,0
cv.imshow("Green",blank)    # background

blank[200:300,300:400]=0,0,255  # bgr blue green red
cv.imshow("Box",blank)


cv.waitKey(0)
