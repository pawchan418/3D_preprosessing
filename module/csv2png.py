import glob
import numpy as np
import cv2

class Csv2Png():

    def __init__(self):
        self.height = 2760

    def convert(self, filename, filepath, dir):
        img = np.loadtxt(filepath, dtype='uint16', delimiter=',')
        for y in range(424):
            for x in range(512):
                if img[y, x] == 0:
                    img[y, x] = 0
                elif img[y, x] > self.height - 1000:
                    img[y, x] = 0
                else:
                    img[y, x] = self.height - img[y, x]

        ksize = 3
        img_mask = cv2.medianBlur(img,ksize)

        np.savetxt('{0}/{1}.csv'.format(dir, filename), img, encoding='utf-8', fmt='%d', delimiter=',')
        np.savetxt('{0}/{1}mask.csv'.format(dir, filename), img_mask, encoding='utf-8', fmt='%d', delimiter=',')

        for y in range(424):
            for x in range(512):
                if img_mask[y, x] > 1000:
                    img_mask[y, x] = img_mask[y, x] - 1000
                else:
                    img_mask[y, x] = 0
        gamma = 0.5
        max = 1760
        img_mask_gamma = max * (img_mask / max)**(1/gamma)

        np.savetxt('{0}/{1}mask_gamma.csv'.format(dir, filename), img_mask_gamma, encoding='utf-8',fmt='%0.5f', delimiter=',')
        cv2.imwrite('{0}/{1}gamma.png'.format(dir, filename), img_mask_gamma)