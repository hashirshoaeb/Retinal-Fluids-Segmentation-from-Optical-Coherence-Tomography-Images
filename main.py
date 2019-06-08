import  numpy as np
import cv2 as cv
import scipy.io

mat = scipy.io.loadmat('path/Subject_01.mat',struct_as_record = False)
# https://github.com/scipy/scipy/blob/v1.3.0/scipy/io/matlab/mio.py#L83-L225
final_mat = {key: mat[key] for key in mat if key not in ['__header__','__version__','__globals__']}
# https://stackoverflow.com/questions/8995611/removing-multiple-keys-from-a-dictionary-safely

for key, value in final_mat.items():
    # https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
    print(key ,"corrosponrds to", np.shape(value))
    # cv.imwrite(key+".png",value)


