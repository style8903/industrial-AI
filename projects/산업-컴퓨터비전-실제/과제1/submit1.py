# 과제 1번
# 사용자로부터 R, G, B 중의 하나의 채널을 입력받고 입력받은 채널에 대한
# 히스토그램을 그리고 평탄화를 한 후에 그 영상을 출력하시오. (선택받은 채널 이외의 채널 값은 변화하지 않음)

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./Lena.png', cv2.IMREAD_COLOR)
b_image, g_image, r_image = cv2.split(image)

print('채널을 입력하세요(R or G or B)')
rgb = input()

if(rgb == 'R'):
    hist = cv2.calcHist([image], [0], None, [256],[0,256])
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
    image_eq = cv2.equalizeHist(r_image)
    hist = cv2.calcHist([image_eq], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
    merge_image = cv2.merge((b_image,g_image,image_eq))
    cv2.imshow('img', merge_image)
    cv2.waitKey()
elif(rgb == 'G'):
    hist = cv2.calcHist([image], [1], None, [256],[0,256])
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
    image_eq = cv2.equalizeHist(g_image)
    hist = cv2.calcHist([image_eq], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
    merge_image = cv2.merge((b_image,image_eq,r_image))
    cv2.imshow('img', merge_image)
    cv2.waitKey()
elif(rgb == 'B'):
    hist = cv2.calcHist([image], [0], None, [256],[0,256])
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
    image_eq = cv2.equalizeHist(b_image)
    hist = cv2.calcHist([image_eq], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
    merge_image = cv2.merge((image_eq,g_image,r_image))
    cv2.imshow('img', merge_image)
    cv2.waitKey()




