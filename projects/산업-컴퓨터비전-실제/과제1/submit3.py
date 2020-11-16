#DFT를 통해서 영상을 주파수 도메인으로 바꿔서 출력 한 후에 사용자로부터 반지름을 입력받아서
# 그 크기만큼의 원을 그린 후에 DFT 결과에 곱해준 후에 IDFT를 해서 필터링된 영상을 출력하시오.
# 사용자로부터 Low pass인지 High Pass인지를 입력받아 Low pass면 원 안을 통과시키고, High Pass면 원 바깥을 통과시키도록 하시오.

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./image_Peppers512rgb.png',0).astype(np.float32)/255
fft = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)
fft_shift = np.fft.fftshift(fft, axes=[0,1])

mask = np.zeros(fft_shift.shape, np.uint8)
y,x = np.ogrid[:mask.shape[0], :mask.shape[1]]
circle = np.sqrt((x - mask.shape[0]//2)**2 + (y-mask.shape[1]//2)**2)

print('반지름값 : ')
r = int(input())

print('Low or High (L,H) : ')
if(input() == 'L'):
    circle_mask = circle <= r
    mask[circle_mask] = 1
elif(input() == 'H'):
    circle_mask = circle >= r
    mask[circle_mask] = 1


fft_shift *= mask
fft = np.fft.ifftshift(fft_shift, axes=[0,1])
filtered = cv2.idft(fft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)

plt.figure()
plt.subplot(121)
plt.axis('off')
plt.title('origin')
plt.imshow(image, cmap='gray')
plt.subplot(122)
plt.axis('off')
plt.title('filtered')
plt.imshow(filtered, cmap='gray')
plt.tight_layout
plt.show()




