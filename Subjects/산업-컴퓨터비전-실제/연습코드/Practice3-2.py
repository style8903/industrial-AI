import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

image = cv2.imread('./Lena.png')

KSIZE = 11
ALPHA = 3
kernel = cv2.getGaussianKernel(KSIZE, 0)
kernel = -ALPHA * kernel @ kernel.T
kernel[KSIZE//2 , KSIZE//2] += 1 + ALPHA
print(kernel.shape, kernel.dtype, kernel.sum())

filetered = cv2.filter2D(image, -1, kernel)

plt.figure(figsize=(8,4))
plt.subplot(121)
plt.axis('off')
plt.title('image')
plt.imshow(image[:,:,[2,1,0]])
plt.subplot(122)
plt.axis('off')
plt.title('filtered')
plt.imshow(filetered[:,:,[2,1,0]])
plt.tight_layout(True)
plt.show()

#cv2.imshow('before', image)
#cv2.imshow('after', filetered)
cv2.waitKey()
cv2.destroyAllWindows()