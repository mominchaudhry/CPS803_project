def load_dataset(verbose=False):
    rootDir = 'Images'
    images = np.zeros((1, 1280), dtype=np.uint8)
    labels = np.empty(20580, dtype=object)
    i = 0
    j = 0
    sift = cv2.SIFT_create(10)
    for dirName, subdirList, fileList in os.walk(rootDir):
        #print('Found directory: %s' % dirName)
        if dirName != 'Images':
            l = dirName.split('-')
            label = l[1]
#             if j == 5:
#                 break
            j += 1
            print(label, j)
        count = 0
        for fname in fileList:
            if dirName != 'Images':
                img = cv2.imread(dirName + '/' + fname, 1)
                file = open("Annotation\\" + dirName.replace('Images\\', '') + "\\" + fname.replace('.jpg', '')).read()
                bnd = [s.strip() for s in re.findall(r'<bndbox>(.*)</bndbox>', file, re.DOTALL)][0].replace('<', ' ').replace('>', ' ').split()
                bndbox = [bnd[1], bnd[4], bnd[7], bnd[10]]
                im3 = img[int(bndbox[1]):int(bndbox[3]), int(bndbox[0]):int(bndbox[2])]
                im = Image.fromarray(im3)
                im.save(dirName + '/' + fname)