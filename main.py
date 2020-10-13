import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image



def load_dataset():
    rootDir = 'Images'
    bigim = np.zeros((1300, 1500, 3))
    images = np.zeros((20580, 1300, 1500, 3))
    labels = np.empty(20580, dtype=np.str)
    i = 0
    for dirName, subdirList, fileList in os.walk(rootDir):
        #print('Found directory: %s' % dirName)
        if dirName != 'Images':
            l = dirName.split('-')
            label = l[1]
            print(label)
        for fname in fileList:
            print('\t%s' % fname)
            if dirName != 'Images':
                im = plt.imread(dirName + '/' + fname)
                bigim[0:len(im), 0:np.size(im, 1), :] = im
                images[i] = bigim
                labels[i] = label
                i += 1

def main():
    """ Main program """
    # Code goes over here.
    print("cyka!")
    load_dataset()
    return 0

if __name__ == "__main__":
    main()