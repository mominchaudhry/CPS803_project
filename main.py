import os
import numpy as np

def load_dataset():
    rootDir = 'Images'
    for dirName, subdirList, fileList in os.walk(rootDir):
        #print('Found directory: %s' % dirName)
        if dirName != 'Images':
            l = dirName.split('-')
            label = l[1]
            print(label)

def main():
    """ Main program """
    # Code goes over here.
    print("cyka!")
    load_dataset()
    return 0

if __name__ == "__main__":
    main()