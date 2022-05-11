# 과제 1번
# 각 픽셀에 임의의 값을 더해 노이즈를 생성하고, 사용자로부터
# Bilateral filtering을 위한 diameter, SigmaColor, SigmaSpace를 입력받아
# 노이즈를 제거하고 노이즈 제거 전후의 영상을 출력하시오.
# (다양한 파라미터 변화를 통해 영상이 어떻게 변화하는지 보고서에 넣으시오.)

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./image_House256rgb.png').astype(np.float32)/255

print('diameter값 : ')
diameter_input = int(input())

print('SigmaColor값 : ')
sigmacolor_input = float(input())

print('SigmaSpace값 : ')
sigmaspace_input = int(input())

noised = (image + 0.2 * np.random.rand(*image.shape).astype(np.float32))
noised = noised.clip(0,1)
plt.imshow(noised[:,:,[2,1,0]])
plt.show()

bilat = cv2.bilateralFilter(noised,diameter_input, sigmacolor_input, sigmaspace_input)
plt.imshow(bilat[:,:,[2,1,0]])
plt.show()