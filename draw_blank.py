import cv2 as cv
from cv2 import FILLED
import numpy as np

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat ', img)

# cv.waitKey(0)



# create  ablank image

blank = np.zeros((500,500,3), dtype='uint8')

# # blank [:] = (0,0,255)

# blank[200:300, 300:400] = 0,0,255

# cv.imshow ('Blank', blank)

# cv .waitKey(0)


# draw a rectangle

cv.rectangle (blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=FILLED)
cv.imshow('Rectangle', blank)


# # draw a circle

cv.circle (blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)

cv.imshow('Circle', blank)


cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)

cv.imshow('Line', blank)




# cv.waitKey(0)




# convert  bgr to gray
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow('gray', gray)

cv.waitKey(0)
