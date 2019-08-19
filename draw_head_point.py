import cv2
import face_recognition
import sys


def main():
    cv2.namedWindow("image")
    for path in sys.argv[1:]:
        image = cv2.imread(path)
        face_landmarks_list = face_recognition.face_landmarks(image)
        ls = list(face_landmarks_list[0].values())
        ret = []
        for i in ls:
            for j in i:
                ret.append(round((j[0]), 3))
                ret.append(round((j[1]), 3))
        print(ret)
        point_size = 1
        point_color = (0, 0, 255)  # BGR
        thickness = 4  # 可以为 0 、4、8


        for i in range(0, len(ret), 2):
            cv2.circle(image, (int(ret[i]), int(ret[i + 1])), point_size, point_color, thickness)
        cv2.imshow('image', image)
        cv2.waitKey(0)


if __name__ == "__main__":
    main()