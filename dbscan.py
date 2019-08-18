import sys
import os
import cv2
import face_recognition
#from sklearn.cluster import DBSCAN
import numpy as np
import shutil

import dlib
import database

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

    # clt = DBSCAN(metric="euclidean", eps=0.4, min_samples=2)
    # clt.fit(ret)
    # labels = clt.labels_
    # labelIDs = np.unique(clt.labels_)
    # numUniqueFaces = len(np.where(labelIDs > -1)[0])
    # #print("[INFO] # unique faces: {}".format(numUniqueFaces))
    #
    # result_path = dest
    # if os.path.exists(result_path):
    #     shutil.rmtree(result_path)
    #
    # os.mkdir(result_path)
    #
    # embd_list = []
    #
    # if 0 not in labelIDs:
    #     print("not exist")
    #
    # for labelID in labelIDs:
    #     if labelID < 0:
    #         index = "negative" + str(-labelID)
    #     else:
    #         index = str(labelID)
    #     try:
    #         index_path = os.path.join(result_path, str(index))
    #         os.mkdir(index_path)
    #     except Exception:
    #         pass
    #     #print("[INFO] faces for face ID: {}".format(labelID))
    #     idxs = np.where(labels == labelID)[0]
    #
    #     select = [ret[i] for i in idxs]
    #     select = np.mean(select, axis=0)
    #     embd_list.append(select)
    #
    #     for i in idxs:
    #         dst = os.path.join(index_path, file_name[i].split("/")[-1])
    #         shutil.copyfile(file_name[i], dst)
    #     #print("embd is " + str(select))
    #
    # if len(embd_list) > 1:
    #     return embd_list[0]
    # else:
    #     return None


if __name__ == "__main__":
    db = database.EmbdingDatabase("star.db")
    db.open(drop_exist=True)
    if False:
        path = sys.argv[1]
        process(path)
    else:
        file_list = os.listdir(sys.argv[1])
        for f in file_list:
            if not f.endswith("jpg"):
                continue
            print(f)
            img = cv2.imread(os.path.join(sys.argv[1], f))
            face_rects = face_recognition.face_locations(img)

            face_index = None
            x, y, w, h = 0, 0, 0, 0
            if len(face_rects) > 0:
                max_size = 0
                for face_rect in face_rects:
                    x, y, w, h = face_rect[3], face_rect[0], face_rect[1] - face_rect[3], face_rect[2] - face_rect[0]
                    if w * h > max_size:
                        max_size = w * h
                        face_index = face_rect

            if face_index is None:
                print(1)
                continue

            # if faceIndex is not None:
            #    cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 3)

            img = img[(y):(y + h), (x):(x + w)]
            ret = face_recognition.face_encodings(img)
            if len(ret) == 0:
                print(2)

                continue

            embd = dlib.vector(ret[0])
            if embd is None:
                print(3)

                continue
            embd = np.array(embd)
            if embd is None:
                print(4)

                continue
            # embd = embd.tostring().encode("base64")
            name = f.replace("_", " ")
            name = name[:-4]
            db.insert(name, embd)

