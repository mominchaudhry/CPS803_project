import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import re
import time
from PIL import Image



def load_dataset(verbose=False):
    rootDir = 'Images'
    images = np.zeros((1, 160, 160, 3), dtype=np.uint8)
    labels = np.empty(20580, dtype=np.str)
    i = 0
    for dirName, subdirList, fileList in os.walk(rootDir):
        #print('Found directory: %s' % dirName)
        if dirName != 'Images':
            l = dirName.split('-')
            label = l[1]
            print(label)
        for fname in fileList:
            if dirName != 'Images':
                img = cv2.imread(dirName + '/' + fname)
                bnd = [s.strip() for s in re.findall(r'<bndbox>(.*)</bndbox>', open("Annotation\\" + dirName.replace('Images\\', '') + "\\" + fname.replace('.jpg', '')).read(), re.DOTALL)][0].replace('<', ' ').replace('>', ' ').split()
                bndbox = [bnd[1], bnd[4], bnd[7], bnd[10]]
                im3 = img[int(bndbox[1]):int(bndbox[3]), int(bndbox[0]):int(bndbox[2]), :]
                if verbose == True:
                    print(fname, i)
                im = cv2.resize(im3, dsize=(160, 160), interpolation=cv2.INTER_CUBIC)
                im = np.reshape(im, (1, 160, 160, 3))
                images = np.append(images, im, axis=0)
                labels[i] = label
                i += 1
    return images[1:,:,:,:], labels

def main():
    """ Main program """
    # Code goes over here.
    load_dataset()
    return 0

if __name__ == "__main__":
    main()