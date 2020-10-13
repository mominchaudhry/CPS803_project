import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image



def load_dataset():
    rootDir = 'Images'
    bigim = np.zeros((1600, 2100, 3))
    images = np.zeros((1, 1600, 2100, 3))
    labels = np.empty(20580, dtype=np.str)
    i = 0
    for dirName, subdirList, fileList in os.walk(rootDir):
        #print('Found directory: %s' % dirName)
        if dirName != 'Images':
            l = dirName.split('-')
            label = l[1]
        for fname in fileList:
            if dirName != 'Images':
                im = plt.imread(dirName + '/' + fname)
                bigim[0:len(im), 0:np.size(im, 1), :] = im
                bigim2 = np.reshape(bigim, (1, 1600, 2100, 3))
                images = np.append(images, bigim2, axis=0)
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