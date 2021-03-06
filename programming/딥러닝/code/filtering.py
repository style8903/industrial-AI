# -*- coding: utf-8 -*-
"""11-10-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l7qhaYZDn8qsWMDPEDuUsnKEdMj9V3hU
"""

from tensorflow.keras.datasets import fashion_mnist
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

plt.imshow(x_train[0])

import numpy as np
import cv2
horizontal_filter = np.array([[1.,2.,1.], [0., 0., 0.], [-1., -2., -1.]])
vertical_filter = np.array([[1.,0.,-1.], [2.,0.,-2.], [1., 0., -1.]])
x_train[0].shape

test_image = cv2.resize(x_train[0], (27,27))
image_size = test_image.shape[0]
#아웃풋 사이즈 : 인풋 사이즈 - 필터 사이즈 + 2*패딩 / 스트라이드 + 1
output_size = int((image_size - 3)/1 + 1)

filter_size = 3

def get_filtered_image(filter):
  filtered_image = np.zeros((output_size, output_size))

  for i in range(output_size):
    for j in range(output_size):
      #컨볼루션 연상
      indice_image = test_image[i:(i+filter_size), j:(j+filter_size)] * filter
      indice_sum = np.sum(indice_image)

      if(indice_sum > 255):
        indice_sum = 255

      filtered_image[i, j] = indice_sum
  
  return filtered_image

vertical_filtered_image = get_filtered_image(vertical_filter)
horizontal_filtered_image = get_filtered_image(horizontal_filter)

plt.subplot(1,3,1)
plt.title('origin')
plt.imshow(x_train[0])

plt.subplot(1,3,2)
plt.title('vertical')
plt.imshow(vertical_filtered_image)

plt.subplot(1,3,3)
plt.title('horizontal')
plt.imshow(horizontal_filtered_image)

plt.show()

sobel_image = np.sqrt(np.square(horizontal_filtered_image) + np.square(vertical_filtered_image))
plt.imshow(sobel_image)

image = x_train[0]
image_x = image.shape[0]
image_y = image.shape[1]

new_image_x = int(image_x / 2)
new_image_y = int(image_y / 2)

pooled_image = np.zeros((new_image_x, new_image_y))

for x in range(0, image_x, 2):
  for y in range(0, image_y, 2):
    pooled_image[int(x/2), int(y/2)] = np.max(image[x:x+2, y:y+2])

plt.imshow(pooled_image)



