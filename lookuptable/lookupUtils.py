from PIL import Image
import numpy as np
import math


def generate_default(dimension):
    if dimension == 512:
        arr = np.ndarray(shape=(512, 512, 4), dtype=np.uint8)
        for by in range(0, 8):
            for bx in range(0, 8):
                for g in range(0, 64):
                    for r in range (0, 64):
                        rr = int(round(r * 255.0 / 63.0))
                        gg = int(round(g * 255.0 / 63.0))
                        bb = int(round(((bx + by * 8.0) * 255.0 / 63.0)))
                        x = r + bx * 64
                        y = g + by * 64
                        arr[y][x][0] = rr
                        arr[y][x][1] = gg
                        arr[y][x][2] = bb
    elif dimension == 64:
        arr = np.ndarray(shape=(64, 64, 4), dtype=np.uint8)
        for by in range(0, 4):
            for bx in range(0, 4):
                for g in range(0, 16):
                    for r in range(0, 16):
                        rr = int(round(r * 255.0 / 16.0))
                        gg = int(round(g * 255.0 / 16.0))
                        bb = int(round(((bx + by * 4.0) * 255.0 / 16.0)))
                        x = r + bx * 16
                        y = g + by * 16
                        arr[y][x][0] = rr
                        arr[y][x][1] = gg
                        arr[y][x][2] = bb
    elif dimension == 8:
        arr = np.ndarray(shape=(8, 8, 4), dtype=np.uint8)
        for by in range(0, 2):
            for bx in range(0, 2):
                for g in range(0, 4):
                    for r in range(0, 4):
                        rr = int(round(r * 255.0 / 4.0))
                        gg = int(round(g * 255.0 / 4.0))
                        bb = int(round(((bx + by * 2.0) * 255.0 / 3.0)))
                        x = r + bx * 4
                        y = g + by * 4
                        arr[y][x][0] = rr
                        arr[y][x][1] = gg
                        arr[y][x][2] = bb
    else:
        return
    img = Image.fromarray(arr)
    img.save(str(dimension)+".bmp", "bmp")


def mix(a, b, f):
    print a, b, f
    ret = np.ndarray(shape=3)
    for i in range(0, 3):
        ret[i] = round(a[i]*(1-f) + b[i]*f)

    return ret;


def apply_512_lookup(image_path, lookup_path):
    image = Image.open(image_path)
    lookup = Image.open(lookup_path)
    image2 = np.array(image)
    lookup2 = np.array(lookup)
    result = np.ndarray(shape=(image2.shape[0], image2.shape[1], 3), dtype=np.uint8)
    for h in range (0, image2.shape[0]):
        for w in range(0, image2.shape[1]):
            print "***begin***"
            color = image2[h][w]
            color255 = color
            print color255
            # print "*************begin***************"
            # print "origin color", color
            color = color / 255.0
            blue = color[2] * 63.0

            quad1 = np.ndarray(shape=2, dtype=np.uint8)
            quad1[1] = math.floor(math.floor(blue) / 8.0)
            quad1[0] = math.floor(blue) - (quad1[1] * 8.0)

            quad2 = np.ndarray(shape=2, dtype=np.uint8)
            quad2[1] = math.floor(math.ceil(blue) / 8.0)
            quad2[0] = math.ceil(blue) - (quad2[1] * 8.0)

            pos1 = np.ndarray(shape=2, dtype=np.float32)
            pos1[0] = quad1[0] * 0.125 + 0.5/512.0 + ((0.125 - 1.0/512.0) * color[0])
            pos1[1] = quad1[1] * 0.125 + 0.5/512.0 + ((0.125 - 1.0/512.0) * color[1])

            pos2 = np.ndarray(shape=2, dtype=np.float32)
            pos2[0] = quad2[0] * 0.125 + 0.5 / 512.0 + ((0.125 - 1.0 / 512.0) * color[0])
            pos2[1] = quad2[1] * 0.125 + 0.5 / 512.0 + ((0.125 - 1.0 / 512.0) * color[1])
            print "index", w, h, int(pos1[1]*512), int(pos1[0]*512), int(pos2[1]*512),int(pos2[0]*512)
            color1 = lookup2[int(pos1[1]*512)][int(pos1[0]*512)]
            color2 = lookup2[int(pos2[1]*512)][int(pos2[0]*512)]

            # print "cal color", pos1*512, pos2*512, color1, color2, blue - math.floor(blue)
            result[h][w] =mix(color1, color2, blue - math.floor(blue))
            print result[h][w]
            print "****end****"
            # print result[h][w]
            # print "*************end*****************"
            # print "\n"
            # print "\n"

    img = Image.fromarray(result)
#   img.show()
    img.save(lookup_path.split(".")[0] + ".bmp", "bmp")


if __name__ == "__main__":
    generate_default(64)
#   generate_default(512)
#   apply_512_lookup("512.bmp", "512_lookup.png")
#   apply_512_lookup("64.bmp", "512_lookup.png")

