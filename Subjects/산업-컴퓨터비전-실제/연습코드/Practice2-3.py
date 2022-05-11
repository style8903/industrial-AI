import cv2, numpy as np
import matplotlib.pyplot as plt

grey = cv2.imread('./Lena.png', 0)
cv2.imshow('org grey', grey)
cv2.waitKey()

hist, bins = np.histogram(grey, 256, [0, 255])
plt.fill(hist)
plt.xlabel('pixel value')
plt.show()

grey_eq = cv2.equalizeHist(grey)
hist, bins = np.histogram(grey_eq, 256, [0, 255])
plt.fill_between(range(256), hist, 0)
plt.xlabel('pixel value')
plt.show()

cv2.imshow('eq grey', grey_eq)
cv2.waitKey()

color = cv2.imread('./Lena.png')
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

hsv[..., 2] = cv2.equalizeHist(hsv[..., 2])
color_eq = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('org color',color)
cv2.imshow('eq color', color_eq)
cv2.waitKey()
cv2.destroyAllWindows()