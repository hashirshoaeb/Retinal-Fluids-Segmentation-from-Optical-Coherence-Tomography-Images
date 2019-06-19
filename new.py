import numpy as np
import cv2
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

#part 1,2
input = plt.imread('images/Subject_01_1.png')
print(input)
# b, g, r = cv.split(input)           # get b,g,r
# rgb_img = cv.merge([r, g, b])     # switch it to rgb
# # Denoising
# dst = cv.fastNlMeansDenoisingColored(input, None, 15, 10, 7, 21)
# b, g, r = cv.split(dst)           # get b,g,r
# rgb_dst = cv.merge([r, g, b])     # switch it to rgb
dst = cv2.fastNlMeansDenoisingColored(input, None, 15, 10, 7, 21)
plt.subplot(121), plt.imshow(input), plt.title('original')
plt.subplot(122), plt.imshow(dst), plt.title('denoise')
plt.show()

#part 3

sobelx64f = cv2.Sobel(dst, cv2.CV_64F, 1, 0, ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

sobely64f = cv2.Sobel(dst, cv2.CV_64F, 0, 1, ksize=5)
abs_sobel64f = np.absolute(sobely64f)
sobel_8y = np.uint8(abs_sobel64f)

plt.subplot(221), plt.imshow(dst, cmap  =  'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(sobel_8u, cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(sobel_8y, cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

#part 4

kernel = np.ones((9, 9), np.uint8)
gradient = cv2.morphologyEx(dst, cv2.MORPH_GRADIENT, kernel)
kernel1 = np.ones((5, 5), np.uint8)
dilation = cv2.erode(gradient, kernel1, iterations=2)
final = gradient-dilation
edges = cv2.Canny(final, 60, 60)
cv2.imshow('Original image', dst)
cv2.imshow('extracted layers', edges)
cv2.waitKey(0)

#plt.subplot(121), plt.imshow(dst), plt.title('original')
#plt.subplot(122), plt.imshow(edges), plt.title('extracted layer')
#plt.show()

#part 5

#gray = cv2.cvtColor(edges, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(edges, 15, 255, cv2.THRESH_BINARY)
cv2.imshow('Original image', edges)
cv2.imshow('binary mask', binary)
cv2.waitKey(0)

#part 6
size = np.shape(input)
print(size)
input = np.arange(120275.0).reshape((283, 425))
image = np.multiply(input, binary)
plt.imshow(image)
plt.show()

#part 7
output = cv2.adaptiveThreshold(binary, 255, cv2.ADAPTIVE_THRESH_MEAN_C,\
             cv2.THRESH_BINARY, 11, 2)
cv2.imshow('thresh', output)
cv2.waitKey(0)

#part 8
actual1 = input.reshape((input.shape[0] * input.shape[1], 1))
output1 = output.reshape((output.shape[0] * output.shape[1], 1))

accuracy = accuracy_score(actual1, output1)
([TP, FP], [FN, TN]) = confusion_matrix(actual1, output1)
# accuracy = (TP+TN)/(TP+TN+FN+FP)
print(accuracy)

kernel = np.ones((9, 9), np.uint8)
gradient1 = cv2.morphologyEx(output, cv2.MORPH_GRADIENT, kernel)
gradient2 = cv2.morphologyEx(input, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('|X}', gradient1)
cv2.imshow('|Y|', gradient2)
cv2.waitKey(0)
gradient2 = np.arange(120275.0).reshape((283, 425))
img_bwo = cv2.bitwise_and(input, input, output)
cv2.imshow('and', img_bwo)
cv2.waitKey(0)