import  numpy as np
import cv2 as cv
import scipy.io

mat = scipy.io.loadmat('path/Subject_02.mat')
print (mat.keys())
print(mat['__version__'])
for i in mat.keys():
    print(mat[i])


