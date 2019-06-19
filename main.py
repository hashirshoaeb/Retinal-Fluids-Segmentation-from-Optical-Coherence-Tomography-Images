import numpy as np
import cv2 as cv
import scipy.io
import matplotlib.pyplot as plt
import math as m

# ----------- 1
mat = scipy.io.loadmat('path/Subject_01.mat',struct_as_record = False)
# https://github.com/scipy/scipy/blob/v1.3.0/scipy/io/matlab/mio.py#L83-L225
final_mat = {key: mat[key] for key in mat if key not in ['__header__','__version__','__globals__']}
# https://stackoverflow.com/questions/8995611/removing-multiple-keys-from-a-dictionary-safely

for key, value in final_mat.items():
    # https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
    print(key ,"corrosponrds to", np.shape(value))
    # cv.imwrite(key+".png",value)

images = final_mat['images']
# 'images' has 61 gray level images with dimension 496, 768
row, col, total_images = np.shape(images)

for i in range(total_images):
    cv.imwrite("images/Subject_01_" + str(i + 1) + ".png", images[:,:,i])
    # images saved in image folder

# ----------- 3
oneimage = cv.imread('images/Subject_01_1.png')
sobelx = cv.Sobel(oneimage,cv.CV_64F,1,0,ksize=3)
sobely = cv.Sobel(oneimage,cv.CV_64F,0,1,ksize=3)
gradmag = np.sqrt(sobelx ** 2 + sobely ** 2)
cv.imwrite("magnitude.png",gradmag)


# ----------- 4
kernel = np.ones((9, 9), np.uint8)
gradient = cv.morphologyEx(oneimage, cv.MORPH_GRADIENT, kernel)
kernel1 = np.ones((5, 5), np.uint8)
dilation = cv.erode(gradient, kernel1, iterations=2)
final = gradient-dilation
edges = cv.Canny(final, 60, 60)
cv.imwrite("edges.png",edges)

# ----------- 5
ret, binary = cv.threshold(edges, 15, 255, cv.THRESH_BINARY)
cv.imwrite("binary.png",binary)
# image = final_mat['manualFluid1']
# images = image[:,:,16]
# # print(np.shape(images))
# row , col = np.shape(images)
# for i in range(row):
#     for j in range(col):
#         if m.isnan(images[i, j]) == True:
#             images[i, j] = 0
#         else:
#             print(images[i,j])
#
# cv.imwrite('gray.png', images)


