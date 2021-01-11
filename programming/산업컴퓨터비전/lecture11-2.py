import cv2
import numpy as np
import os

pattern_size = (8, 6)
samples = []

file_list = os.listdir('./fisheyes')
img_file_list = [file for file in file_list if file.startswith('Fisheye2_')]

for filename in img_file_list:

    frame = cv2.imread(os.path.join('./fisheyes', filename))
    res, corners = cv2.findChessboardCorners(frame, pattern_size)

    img_show = np.copy(frame)
    cv2.drawChessboardCorners(img_show, pattern_size, corners, res)
    cv2.putText(img_show, 'Samples captured: %d' % len(samples), (0, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
    cv2.imshow('chessboard', img_show)

    wait_time = 0 if res else 30
    k = cv2.waitKey(wait_time)

    if k == ord('s') and res:
        samples.append((cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), corners))
    elif k == 27:
        break

cv2.destroyAllWindows()

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 1e-6)

for i in range(len(samples)):
    img, corners = samples[i]
    corners = cv2.cornerSubPix(img, corners, (10, 10), (-1, -1), criteria)

pattern_points = np.zeros((1, np.prod(pattern_size), 3), np.float32)
pattern_points[0, :, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)

images, corners = zip(*samples)

pattern_points = [pattern_points] * len(corners)

print(len(pattern_points), pattern_points[0].shape, pattern_points[0].dtype)
print(len(corners), corners[0].shape, corners[0].dtype)

camera_matrix = np.zeros((3, 3))
dist_coefs = np.zeros([1, 4])
xi = np.zeros(1)
rvecs = [np.zeros((1, 1, 3), dtype=np.float32) for i in range(len(corners))]
tvecs = [np.zeros((1, 1, 3), dtype=np.float32) for i in range(len(corners))]

rms = cv2.omnidir.calibrate(
    pattern_points, corners, images[0].shape, camera_matrix, xi, dist_coefs, cv2.omnidir.RECTIFY_PERSPECTIVE,
    (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 60, 0.000001), rvecs, tvecs)

np.save('camera_mat.npy', camera_matrix)
np.save('dist_coefs.npy', dist_coefs)

print(np.load('camera_mat.npy'))
print(np.load('dist_coefs.npy'))

img = cv2.imread('./fisheyes/Fisheye2_2.jpg')
new_camera_matrix = np.copy(camera_matrix)
new_camera_matrix[0, 0] = new_camera_matrix[0, 0] / 3
new_camera_matrix[1, 1] = new_camera_matrix[1, 1] / 3
print(new_camera_matrix)
print(camera_matrix)
undistorted = np.zeros((640, 480, 3), np.uint8)
undistorted = cv2.omnidir.undistortImage(img, camera_matrix, dist_coefs, xi, cv2.omnidir.RECTIFY_PERSPECTIVE, undistorted, new_camera_matrix)

cv2.imshow("undistorted", undistorted)
cv2.waitKey(0)