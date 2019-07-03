import cv2
import os
import sys
import face_recognition


def foo(arr):
    for i in range(0, len(arr)):
        img = cv2.imread(arr[i])
        if img is None:
            continue

        # classfier = cv2.CascadeClassifier("/usr/local/Cellar/opencv@3/3.4.5_1/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml")
        #
        # faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        faceRects = face_recognition.face_locations(img)

        faceIndex = None
        x, y, w, h = 0,0,0,0
        if len(faceRects) > 0:
            maxSize = 0;
            for faceRect in faceRects:
                x, y, w, h = faceRect[3],faceRect[0], faceRect[1]-faceRect[3], faceRect[2]-faceRect[0]
                if w * h > maxSize:
                    maxSize = w * h
                    faceIndex = faceRect

        if faceIndex is None:
            continue

        #if faceIndex is not None:
        #    cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 3)

        img2 = img[ (y):(y + h),(x):(x + w)]
        rindex = arr[i].rfind("/")
        path = arr[i][0:rindex] + "/" + "test/"
        if not os.path.exists(path):
            os.mkdir(path)
        path = path + arr[i].split("/")[-1]
        print path

        h, w, depth = img2.shape
        if w <= 0:
            continue
        if h <= 0:
            continue
        print(img2.shape)
        img2 = cv2.resize(img2, (64, 64), interpolation=cv2.INTER_AREA)
        cv2.imwrite(path, img2)
        #ret = face_recognition.face_encodings(img2)
        #print(ret)

        if 2 > 11:
            cv2.namedWindow("Image")
            cv2.imshow("Image", img2)
            cv2.waitKey (0)
            cv2.destroyAllWindows()


try:
    path = sys.argv[1]
    arr = []
    if os.path.isfile(path):
        arr.append(path)
    else:
        files = os.listdir(path)

        for file in files:
            full_path = path + "/" + file
            if os.path.isfile(full_path):
                arr.append(full_path)
    foo(arr)
except AssertionError:
    pass

