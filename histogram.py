from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys
import math

print sys.argv[1]

showRGB = False
shouBrightNess = True
src = Image.open(sys.argv[1])
data = src.split()
if len(data) == 3:
    r, g, b = data
elif len(data) == 4:
    r, g, b, a = data

size = src.size
imb = Image.new('RGB', size)


pima = src.load()
pimb = imb.load()

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


left = 50
distance = 155

ratio = 1
changable = 50;

point_size = size[0] * size[1]
points = []



for i in range(0,256):
    points.append(0)


for i in range(size[0]):
    for j in range(size[1]):


        #make to middle
        a = pima[i,j]
        pimb[i, j] = (a[0] + int(math.cos(a[0]/256.0*math.pi)*changable*ratio), a[1] + int(math.cos(a[1]/256.0*math.pi)*changable*ratio), a[2] + int(math.cos(a[2]/256.0*math.pi)*changable*ratio))

        a = pimb[i, j]
        bright = (a[0] + a[1] + a[2])/3
        points[bright] = points[bright] + 1;


output = sys.argv[1] + ".bmp"
imb.save(output)

src = Image.open(output)
imb = Image.new('RGB', size)
pima = src.load()
pimb = imb.load()


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
    plt.figure("brightness2")
    arr = img.flatten()
    n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor='green', alpha=0.75)

if showRGB or shouBrightNess:
    plt.show()

i = 0
sum = 0;
ratio = 0.1
for i in range (0, 256):
    sum += points[i]
    if sum > point_size * ratio:
        break
left_disguard = i

ratio = 0.0005
i = 0
sum = 0
for i in range(255, -1, -1):
    sum += points[i]
    if sum > point_size * ratio:
        break

right_disguard = i
distance = right_disguard - left_disguard

print left_disguard, right_disguard

for i in range(size[0]):
    for j in range(size[1]):
        a = pima[i, j]
        pimb[i, j] = ((a[0] - left_disguard) * 256 / distance, (a[1] - left_disguard) * 256 / distance, (a[2] - left_disguard) * 256 / distance)



output = sys.argv[1] + ".bmp.bmp"
imb.save(output)

src = Image.open(output)

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
    plt.figure("brightness2")
    arr = img.flatten()
    n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor='green', alpha=0.75)

if showRGB or shouBrightNess:
    plt.show()

