import numpy as np
import cv2 as cv



# yourimage     givenImage      label       number
# 0             0               TN          2*0 + 0 = 0
# 0             1               FN          2*0 + 1 = 1
# 1             0               FP          2*1 + 0 = 2
# 1             1               TP          2*1 + 1 = 3
# where 0 is background 1 is foreground

# yourimage     givenImage      label       number
# 255           255             TN          2*255 + 255 = 765 = 253 + 3 = 0 *63 = 0(as ans will not exceed 255)
# 255           0               FN          2*255 + 0 = 510 = 254 + 3 = 1 *63 = 63
# 0             255             FP          2*0 + 255 = 255 = 255 + 3 = 2 *63 = 126
# 0             0               TP          2*0 + 0 = 0 = 0 + 3 = 3 *63 = 189
# where 255 is background 0 is foreground
def performancePrams(yourImage, givenImage):
    output = (((yourImage * 2) + givenImage) + 3)*63
    unique_elements, counts = np.unique(output, return_counts=True)
    print(unique_elements, counts)
    TN, FN, FP, TP = counts
    # TPR = TP / (TP + FN)
    # FPR = FP / (TN + FP)
    # diceCoff = 2*TP / (FN + (2*TP) + FP)
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    # print([TPR, FPR, diceCoff])
    print("accuracy = ", accuracy)
    return output

