import cv2 as cv
import numpy as np
# RECTANGLE
img=np.zeros((500,500,3),dtype="uint8")
cv.rectangle(img,(100,100),(150,200),(255,0,0),
             thickness=cv.FILLED)
            # also we can write -1 instead of cv.FILLED
cv.imshow("Rectangle",img)
#Circle
circle1=cv.circle(img,(50,50),10,(255,255,255),thickness=cv.FILLED)
cv.imshow("Circle",circle1)
#Line
line=cv.line(img,(100,250),(50,150),(0,0,255),thickness=2)
cv.imshow("Line",line)
cv.waitKey(0)