from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
showRGB = False
shouBrightNess = True
src = Image.open('/tmp/a.png')
data = src.split()
if len(data) == 3:
    r, g, b = data
elif len(a) == 4:
    r, g, b, a = data

r, g, b = src.split()

if showRGB:
    plt.figure("rgb")
    ar = np.array(r).flatten()
    plt.hist(ar, bins=256, normed=1,facecolor='r',edgecolor='r',hold=1)
    ag = np.array(g).flatten()
    plt.hist(ag, bins=256, normed=1, facecolor='g',edgecolor='g',hold=1)
    ab = np.array(b).flatten()
    plt.hist(ab, bins=256, normed=1, facecolor='b',edgecolor='b')

if shouBrightNess:
    img = np.array(src.convert('L'))
    plt.figure("brightness")
    arr = img.flatten()
    n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor='green', alpha=0.75)

if showRGB or shouBrightNess:
    plt.show()
