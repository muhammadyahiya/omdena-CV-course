import cv2

img = cv2.imread('Resources/Photos/cat.jpg')

cv2.imshow('Cat', img)

cv2.waitkey()