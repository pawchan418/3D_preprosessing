import glob
import numpy as np
import cv2

file_list = glob.glob('*delete.csv')
#%%heightstr = input('height:')
#%%height = int(heightstr)
height = 2760
print(file_list)

for file_name in file_list:
    array = np.loadtxt(file_name, dtype='uint16', delimiter=',')
    print(array)
    for y in range(424):
        for x in range(512):
            if array[y, x] >= height - 300:
                array[y, x] = 0
    
    array2 = array * 23
    array3 = cv2.bitwise_not(array2)
    for y in range(424):
        for x in range(512):
            if array3[y, x] == 65535:
                array3[y, x] = 0
    print(array3)
    cv2.imwrite('{0}.png'.format(file_name), array3)
print('done')