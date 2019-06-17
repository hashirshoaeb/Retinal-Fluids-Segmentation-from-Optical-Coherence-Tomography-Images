import numpy as np
import cv2 as cv
import scipy.io
import matplotlib.pyplot as plt
import math as m

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
print(total_images)
for i in range(total_images):
    cv.imwrite("images/Subject_01_" + str(i + 1) + ".png", images[:,:,i])


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


