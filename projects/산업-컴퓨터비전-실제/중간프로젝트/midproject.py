import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step1. 최초 이미지 로드 및 사이즈 변경
image = cv2.imread('./sample1.PNG',cv2.IMREAD_COLOR)
resized_img = cv2.resize(image, (300,450))

# Step2. 노이즈 제거를 위한 filtering
blur = cv2.bilateralFilter(resized_img, 0, 75, 75)

# Step3. HSV로의 변경
hsv_img = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

# Step4. H값 histogram 분석
hist = cv2.calcHist([hsv_img], [0], None, [177],[0,177])
plt.plot(hist)
plt.xlim([0, 177])
plt.show()


# for a in range(hsv_img.shape[0]):
#     for b in range(hsv_img.shape[1]):
#         if ((hsv_img[a][b][0] < 10)):
#             blur[a][b] = (255,0,0)


# Step5. 마우스 클릭을 통한 HSV값 알아내기
def mouse_callback(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONUP:
        print(x,y)
        print(hsv_img[y][x])

cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_callback)

while(True):
    cv2.imshow('img', blur)
    k = cv2.waitKey(1)

    if k ==27:
        break

cv2.destroyAllWindows()

# Step6. 각각 영역 별 mask 생성 및 영역 추출
area_1_low = (0,90,10)
area_1_high = (10,255,120)
area_1_mask = cv2.inRange(hsv_img, area_1_low, area_1_high)
area_1_img = cv2.bitwise_and(blur, blur, mask=area_1_mask)

area_2_low = (10, 40, 0)
area_2_high = (70, 255, 60)
area_2_mask = cv2.inRange(hsv_img, area_2_low, area_2_high)
area_2_img = cv2.bitwise_and(blur, blur, mask=area_2_mask)

area_3_low = (15, 90, 160)
area_3_high = (25, 180, 190)
area_3_mask = cv2.inRange(hsv_img, area_3_low, area_3_high)
area_3_img = cv2.bitwise_and(blur, blur, mask=area_3_mask)


# Result1. 각각 이미지 생성
# cv2.imshow('img', image)
# cv2.imshow('resized', resized_img)
# cv2.imshow('blur', blur)
# cv2.imshow('hsv', hsv_img)
# # cv2.imshow('area_1', area_1_img)
# # cv2.imshow('area_1', area_2_img)
# # cv2.imshow('area_1', area_3_img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# Result2. 비교 이미지 생성
resized_img= cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
blur = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
area_1_img = cv2.cvtColor(area_1_img, cv2.COLOR_HSV2BGR)
area_2_img = cv2.cvtColor(area_2_img, cv2.COLOR_HSV2BGR)
area_3_img = cv2.cvtColor(area_3_img, cv2.COLOR_HSV2BGR)

plt.figure()
plt.subplot(121)
plt.axis('off')
plt.title('Before')
plt.imshow(blur)
plt.subplot(122)
plt.axis('off')
plt.title('After')
plt.imshow(area_1_img)
plt.show()