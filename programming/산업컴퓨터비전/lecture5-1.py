import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./Lena.png', 0)

otsu_thr, otsu_mask = cv2.threshold(image, -1, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('estimated threshold (otsu): ', otsu_thr)

plt.figure(figsize=(6,3))
plt.subplot(121)
plt.axis('off')
plt.title('origin')
plt.imshow(image, cmap='gray')
plt.subplot(122)
plt.axis('off')
plt.title('otsu threshold')
plt.imshow(otsu_mask, cmap='gray')
plt.tight_layout()
plt.show()