import cv2
import numpy
img = cv2.imread("/Users/mamk/Downloads/a.jpg",0) #The ',0' makes it read the image as a grayscale image
img2 = cv2.imread("/Users/mamk/Downloads/a.jpg");
row, col = img.shape[:2]


def df(img):  # to make a histogram (count distribution frequency)
    values = [0]*256
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            values[img[i,j]]+=1
    return values


def cdf(hist):  # cumulative distribution frequency
    cdf = [0] * len(hist)   #len(hist) is 256
    cdf[0] = hist[0]
    for i in range(1, len(hist)):
        cdf[i]= cdf[i-1]+hist[i]
    # Now we normalize the histogram
    cdf = [ele*255/cdf[-1] for ele in cdf]      # What your function h was doing before
    return cdf

def equalize_image(image):
    my_cdf = cdf(df(img))
    # use linear interpolation of cdf to find new pixel values. Scipy alternative exists
    import numpy as np
    image_equalized = np.interp(image, range(0,256), my_cdf)
    return image_equalized

eq = equalize_image(img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        Y = img2[i, j, 0] * 0.299 + img2[i, j, 1] * 0.587 + img2[i, j, 2] * 0.114
        U = -0.169 * img2[i,j,0] - 0.331 * img2[i,j,1] + 0.5 * img2[i,j,2];
        V = 0.5 * img2[i,j,0] - 0.419 * img2[i,j,1] - 0.081 * img2[i,j,2];

        Y = eq[i, j]
        r = Y + 1.402 * (V)
        g = Y - 0.3441 * (U) - 0.714 * (V)
        b = Y + 1.772 * (U)

        r = numpy.clip(r, 0, 255)
        g = numpy.clip(g, 0, 255)
        b = numpy.clip(b, 0, 255)

        #img2[i,j] = [r, g, b]

        img2[i,j,0] = r
        img2[i,j,1] = g
        img2[i,j,2] = b


cv2.imwrite('equalized.png', img2)