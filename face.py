import cv2
import sys
import numpy as np
def foo():
    for i in range(1, len(sys.argv)):
        img = cv2.imread(sys.argv[i])
        if img is None:
            continue
        color = (0, 255, 0)

        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        classfier = cv2.CascadeClassifier("/usr/local/Cellar/opencv/3.4.2/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml")

        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))

        faceIndex = None
        x, y, w, h = 0,0,0,0
        if len(faceRects) > 0:
            maxSize = 0;
            for faceRect in faceRects:
                x, y, w, h = faceRect
                if w * h > maxSize:
                    maxSize = w * h
                    faceIndex = faceRect

        if faceIndex is None:
            continue

        #if faceIndex is not None:
        #    cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 3)

        img2 = img[ (y - 10):(y + h + 10),(x - 10):(x + w + 10)]
        print sys.argv[1] + "/"+ sys.argv[i].split("/")[-1]
        cv2.imwrite(sys.argv[1] + "/" + sys.argv[i].split("/")[-1], img2)

        if 2 > 11:
            cv2.namedWindow("Image")
            cv2.imshow("Image", img2)
            cv2.waitKey (0)
            cv2.destroyAllWindows()


try:
    foo()
except AssertionError:
    pass

