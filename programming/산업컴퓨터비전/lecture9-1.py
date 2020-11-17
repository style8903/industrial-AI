import cv2
import numpy as np

img = cv2.imread('./scenetext01.jpg', cv2.IMREAD_COLOR)

surf = cv2.xfeatures2d.SURF_create(10000)
surf.setExtended(True)
surf.setNOctaves(3)
surf.setNOctaveLayers(10)
surf.setUpright(False)

keyPoints, descriptors = surf.detectAndCompute(img, None)

show_img = cv2.drawKeypoints(img, keyPoints, None, (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SURF Descriptors', show_img)
cv2.waitKey()
cv2.destroyAllWindows()

brief = cv2.xfeatures2d.BriefDescriptorExtractor_create(32,True)

keyPoints, descriptors = brief.compute(img, keyPoints)
show_img = cv2.drawKeypoints(img, keyPoints, None, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('BRIEF Descriptors', show_img)
cv2.waitKey()
cv2.destroyAllWindows()


orb = cv2.ORB_create()
orb.setMaxFeatures(200)

keyPoints = orb.detect(img, None)
keyPoints, descriptors = orb.compute(img, keyPoints)

show_img = cv2.drawKeypoints(img, keyPoints, None, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('BRIEF Descriptors', show_img)
cv2.waitKey()
cv2.destroyAllWindows()