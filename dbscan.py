import sys
import os
import cv2
import face_recognition
from sklearn.cluster import DBSCAN
import numpy as np
import shutil

import dlib

def calc_embded(file_list):
    embd_list = []
    file_name = []
    for f in file_list:
        img = cv2.imread(f)
        ret = face_recognition.face_encodings(img)
        if len(ret) == 0:
            continue
        file_name.append(f)
        embd_list.append(dlib.vector(ret[0]))
    return file_name, embd_list

def calc_embded2(file_list):
    embd_list = []
    file_name = []
    for f in file_list:
        img = cv2.imread(f)
        ret = face_recognition.face_encodings(img)
        if len(ret) == 0:
            continue
        file_name.append(f)
        embd_list.append(dlib.vector(ret[0]))
    return file_name, embd_list


def distance(a, b):
    vec1 = np.array(a)
    vec2 = np.array(b)
    dist = np.sqrt(np.sum(np.square(vec1 - vec2)))
    return dist

def process(path, dest):
    arr = []
    if os.path.isfile(path):
        arr.append(path)
    else:
        files = os.listdir(path)

        for file in files:
            full_path = os.path.join(path, file)
            if os.path.isfile(full_path):
                arr.append(full_path)

    file_name, ret = calc_embded(arr)
    # labels = dlib.chinese_whispers_clustering(ret, 0.5)
    # labelIDs = np.unique(labels)





    clt = DBSCAN(metric="euclidean", eps=0.4)
    clt.fit(ret)
    labels = clt.labels_
    labelIDs = np.unique(clt.labels_)
    numUniqueFaces = len(np.where(labelIDs > -1)[0])
    print("[INFO] # unique faces: {}".format(numUniqueFaces))

    result_path = dest
    if os.path.exists(result_path):
        shutil.rmtree(result_path)

    os.mkdir(result_path)

    embd_list = []
    for labelID in labelIDs:
        if labelID < 0:
            index = "negative" + str(-labelID)
        else:
            index = str(labelID)
        try:
            index_path = os.path.join(result_path, str(index))
            os.mkdir(index_path)
        except Exception:
            pass
        print("[INFO] faces for face ID: {}".format(labelID))
        idxs = np.where(labels == labelID)[0]

        select = [ret[i] for i in idxs]
        select = np.mean(select, axis=0)
        embd_list.append(select)

        for i in idxs:
            dst = os.path.join(index_path, file_name[i].split("/")[-1])
            shutil.copyfile(file_name[i], dst)
        #print("embd is " + str(select))

    if len(embd_list) > 2:
        print(file_name[i])
        print("one two dist is " + str(distance(embd_list[0], embd_list[1])))

    if len(embd_list) > 1:
        return embd_list[0]
    else:
        return None


if __name__ == "__main__":
    path = sys.argv[1]
    process(path)
