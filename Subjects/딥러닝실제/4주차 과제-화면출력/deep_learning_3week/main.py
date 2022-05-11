# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('./2020254005_ksw.jpg')

plt.imshow(img)
plt.show()

