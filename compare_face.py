import face_recognition
import cv2
import numpy as np
import os

def get_face_embd(file_path):
    img = cv2.imread(file_path)
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
        return

    img2 = img[(y):(y + h), (x):(x + w)]

    if 2 > 11:
        cv2.namedWindow("Image")
        cv2.imshow("Image", img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    ret = face_recognition.face_encodings(img2)
    return ret


def distance(a, b):
    vec1 = np.array(a)
    vec2 = np.array(b)
    dist = np.sqrt(np.sum(np.square(vec1 - vec2)))
    return dist

def get_file_name(path):
    return os.path.basename(path)[:-4]

if __name__ == "__main__":
    path = ["/Users/mamk/Desktop/ldh1.jpg",
            "/Users/mamk/Desktop/ldh2.jpg",
            "/Users/mamk/Desktop/ldh3.jpg",
            "/Users/mamk/Desktop/ldh4.jpg",
            "/Users/mamk/Desktop/lcw1.jpg",
            "/Users/mamk/Desktop/lcw2.jpg",
            "/Users/mamk/Desktop/cz1.jpg",
            "/Users/mamk/Desktop/cz2.jpg",
            "/Users/mamk/Desktop/cz3.jpg",
            "/Users/mamk/Desktop/cz4.jpg",
            "/Users/mamk/Desktop/et.png",
            "/Users/mamk/Desktop/zgr.png"]

    result = []
    for p in path:
        ret = get_face_embd(p)
        result.append(ret)


    for i in range(len(result)):
        for j in range(len(result)):

            show = "%s:%s=%f" %(get_file_name(path[i]), get_file_name(path[j]), distance(result[i], result[j]))
            print(show)

    # print(distance(result[0], result[1]))
    # print(distance(result[0], result[2]))
    # print(distance(result[0], result[3]))
    # print(distance(result[0], result[4]))
    # print(distance(result[0], result[5]))
    # print(distance(result[0], result[6]))
    # print(distance(result[5], result[6]))
    # print(distance(result[7], result[8]))








