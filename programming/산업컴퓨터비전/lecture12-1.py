import cv2
import numpy as np

p1 = np.eye(3,4, dtype=np.float32)
p2 = np.eye(3,4, dtype=np.float32)
p2[0,3] = -1

N = 5
points3d = np.empty((4,N), np.float32)
points3d[:3,:] = np.random.randn(3, N)
points3d[3, :] = 1

points1 = p1 @ points3d
points1 = points1[:2, :] / points1[2, :]
points1[:2,:] += np.random.randn(2, N) * 1e-2


points2 = p2 @ points3d
points2 = points2[:2, :] / points2[2, :]
points2[:2,:] += np.random.randn(2, N) * 1e-2

points3d_reconstr = cv2.triangulatePoints(p1, p2, points1, points2)
points3d_reconstr /= points3d_reconstr[3, :]

print('origin')
print(points3d[:3].T)
print('reco')
print(points3d_reconstr[:3].T)