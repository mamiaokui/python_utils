from PIL import Image
import os
import os.path
import numpy as np




path = r"/tmp/a.png"
im = Image.open(path)
imageData = np.array(im)
for i in range(0, imageData.shape[0]):
    for j in range(0, imageData.shape[1]):
         if imageData[i][j][0]==0 and imageData[i][j][1]==0 and imageData[i][j][2]==0:
             imageData[i][j][3] = 0

im = Image.fromarray(imageData)
im.save("/tmp/abcdefg.png")
