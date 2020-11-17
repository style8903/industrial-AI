import cv2, numpy as np

image = cv2.imread('./Lena.png').astype(np.float32)/255
print('shape', image.shape)
print('data type', image.dtype)
cv2.imshow('origin image', image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print('convert to gray')
print('shape', gray.shape)
print('data type', gray.dtype)
cv2.imshow('gray image', gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print('convert to HSV')
print('shape', hsv.shape)
print('data type', hsv.dtype)
cv2.imshow('hsv image', hsv)

hsv[:,:,0] *= 3
from_hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
print('convert back to BGR from HSV')
print('shape', from_hsv.shape)
print('data type', from_hsv.dtype)
cv2.imshow('from_hsv', from_hsv)
cv2.waitKey()
cv2.destroyAllWindows()