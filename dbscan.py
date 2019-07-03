import sys
import os
import cv2
import face_recognition
from sklearn.cluster import DBSCAN
import numpy as np
import shutil


def foo(file_list):
    embd_list = []
    file_name = []
    for f in file_list:
        img = cv2.imread(f)
        ret = face_recognition.face_encodings(img)
        if len(ret) == 0:
            continue
        file_name.append(f)
        embd_list.append(ret[0])
    return file_name, embd_list


if __name__ == "__main__":
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

    file_name, ret = foo(arr)
    clt = DBSCAN(metric="euclidean", eps=0.4)
    clt.fit(ret)
    labelIDs = np.unique(clt.labels_)
    numUniqueFaces = len(np.where(labelIDs > -1)[0])
    print("[INFO] # unique faces: {}".format(numUniqueFaces))
    if os.path.exists("/tmp/abc"):
        shutil.rmtree('/tmp/abc')

    os.mkdir("/tmp/abc")

    for labelID in labelIDs:
        if labelID < 0:
            index = "negative" + str(-labelID)
        else:
            index = str(labelID)
        try:
            os.mkdir("/tmp/abc/" + str(index))
        except Exception:
            pass
        print("[INFO] faces for face ID: {}".format(labelID))
        idxs = np.where(clt.labels_ == labelID)[0]

        for i in idxs:
            dst = "/tmp/abc/" + index + "/" + file_name[i].split("/")[-1]
            shutil.copyfile(file_name[i], dst)

