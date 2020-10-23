import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image



def load_dataset():
    rootDir = 'Images'
    images = np.zeros((1, 500, 500), dtype=np.uint8)
    labels = np.empty(20580, dtype=np.str)
    i = 0
    for dirName, subdirList, fileList in os.walk(rootDir):
        #print('Found directory: %s' % dirName)
        if dirName != 'Images':
            l = dirName.split('-')
            label = l[1]
        for fname in fileList:
            if dirName != 'Images':
                img = cv2.imread(dirName + '/' + fname)
                im2 = ((img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3).astype(np.uint8)
                im = cv2.resize(im2, dsize=(500, 500), interpolation=cv2.INTER_CUBIC)
                im = np.reshape(im, (1, 500, 500))
                images = np.append(images, im, axis=0)
                labels[i] = label
                print(i)
                i += 1

def main():
    """ Main program """
    # Code goes over here.
    print("cyka!")
    load_dataset()
    return 0

if __name__ == "__main__":
    main()