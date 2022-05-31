import cv2 as cv
"""
Created on Mon May 23 21:05:59 2022

@author: nusre
"""
img=cv.imread("cat.jpg")   # dimensions = 720*640 we can easily see.

cv.imshow("Cat",img)

img2=cv.imread("cat_large.jpg") # dimensions = 1600*1062 we can't see whole photo
cv.imshow("Large Cat",img2)

cv.waitKey(0)
