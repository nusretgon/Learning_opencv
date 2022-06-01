import cv2 as cv
import numpy as np
# RECTANGLE
img=np.zeros((500,500,3),dtype="uint8")
cv.rectangle(img,(100,100),(150,200),(255,0,0),
             thickness=cv.FILLED)
            # also we can write -1 instead of cv.FILLED
cv.imshow("Rectangle",img)
cv.waitKey(0)