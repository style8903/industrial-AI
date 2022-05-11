import cv2
import numpy as np
import random

img = cv2.imread('./scenetext01.jpg', cv2.IMREAD_COLOR)

fast = cv2.FastFeatureDetector_create(160, True, cv2.FAST_FEATURE_DETECTOR_TYPE_9_16)
keyPoint = fast.detect(img)

for kp in keyPoint:
    kp.size = 100*random.random()
    kp.angle = 360*random.random()

matches = []
for i in range(len(keyPoint)):
    matches.append(cv2.DMatch(i, i, 1))

show_img = cv2.drawKeypoints(img, keyPoint, None, (255,0,255))

cv2.imshow('keypoint', show_img)
cv2.waitKey()
cv2.destroyAllWindows()

show_img = cv2.drawKeypoints(img, keyPoint, None, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('keypoint', show_img)
cv2.waitKey()
cv2.destroyAllWindows()

show_img = cv2.drawMatches(img, keyPoint, img, keyPoint, matches, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('matches', show_img)
cv2.waitKey()
cv2.destroyAllWindows()