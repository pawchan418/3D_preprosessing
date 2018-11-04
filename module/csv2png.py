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
        img_mask20 = img_mask * 20

        gamma = 2.0
        max = 65535
        img_mask20_gamma = max * (img_mask20 / max)**(1/gamma)


        np.savetxt('{0}/{1}.csv'.format(dir, filename), img_mask, delimiter=',')
        cv2.imwrite('{0}/{1}.png'.format(dir, filename), img_mask)
        cv2.imwrite('{0}/{1}20.png'.format(dir, filename), img_mask20)
        cv2.imwrite('{0}/{1}20gamma.png'.format(dir, filename), img_mask20_gamma)