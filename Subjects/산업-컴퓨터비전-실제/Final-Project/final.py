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

# Step4. 영역별 Mask 생성
area_1_low = (0,90,10)
area_1_high = (7,255,120)
area_1_mask = cv2.inRange(hsv_img, area_1_low, area_1_high)
output1 = cv2.bitwise_and(hsv_img,hsv_img, mask=area_1_mask)

area_2_low = (10, 40, 0)
area_2_high = (70, 255, 60)
area_2_mask = cv2.inRange(hsv_img, area_2_low, area_2_high)
output2 = cv2.bitwise_and(hsv_img, hsv_img, mask=area_2_mask)

area_3_low = (15, 100, 160)
area_3_high = (20, 180, 190)
area_3_mask = cv2.inRange(hsv_img, area_3_low, area_3_high)
output3 = cv2.bitwise_and(hsv_img, hsv_img, mask=area_3_mask)

def draw_area(area_mask):
    #Step5. Thresh Hold 수행
    ret, thresh = cv2.threshold(area_mask, 10, 255, 0)
    cv2.imshow('thresh', thresh)

    #Step6. Find Contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(resized_img, contours, -1, (0,255,0), 3)

    max_m = 0
    max_h = 0
    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        # cv2.rectangle(resized_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        if w > max_m:
            max_m = w
        if h > max_h:
            max_h = h

    cv2.rectangle(resized_img, (x, y), (x + max_m, y + max_h), (0, 0, 255), 2)
    print('가로 : %d, 세로 : %d, 면적(mm^2) : %d' %(max_m, max_h, max_m * max_h))

draw_area(area_2_mask)
cv2.imshow('after', resized_img)
cv2.waitKey()
cv2.destroyAllWindows()