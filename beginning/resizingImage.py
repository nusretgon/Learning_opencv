
import cv2
import numpy as np

img = cv2.imread("cat_large.jpg")

imgResize = cv2.resize(img, (500, 500))

cv2.imshow("Image", img)
cv2.imshow("Image Resize",imgResize)


cv2.waitKey(0)