import face_recognition
import cv2
import sys
import os


def algorithm1(path, img):
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
        exit(0)

    left = 3
    right = 3
    top = 4
    bottom = 4
    width = 540
    height = 720
    #####
    middle_x = x + w / 2
    middle_y = y + h / 2

    left_pad = middle_x / left
    right_pad = (img.shape[1] - middle_x) / right
    up_pad = middle_y / top
    bottom_pad = (img.shape[0] - middle_y) / bottom
    min_pad = min(left_pad, right_pad, up_pad, bottom_pad, w)

    x_value = middle_x - min_pad * left;
    y_value = middle_y - min_pad * top
    w_value = min_pad * left + min_pad * right
    h_value = min_pad * top + min_pad * bottom

    img = img[int(y_value):int(y_value + h_value), int(x_value):int(x_value + w_value)]

    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)

    filename = os.path.basename(path)

    output = os.path.join("/tmp/thumbnail", filename)

    cv2.imwrite(output, img)


def algorithm2(path, img):
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
        exit(0)

    left = 3
    right = 3
    top_ceil = 2
    bottom_ceil = 6
    top_expect = 3
    bottom_expect = 5
    top_floor = 4
    bottom_floor = 4
    middle_x = x + w / 2
    middle_y = y + h / 2
    max_value = max(img.shape[0], img.shape[1])
    position_ratio = [w, middle_x/left, (img.shape[1] - middle_x)/right, max_value]
    if middle_y * 1.0 / (img.shape[0] - middle_y) < top_ceil * 1.0 / bottom_ceil:
        position_ratio[3] = middle_y/top_ceil
        top_true = top_ceil
        bottom_true = bottom_ceil
    elif top_floor * 1.0 / bottom_floor < middle_y * 1.0 / (img.shape[0] - middle_y):
        position_ratio[3] = (img.shape[0] - middle_y) /bottom_floor
        top_true = top_floor
        bottom_true = bottom_floor
    else:
        top_true = middle_y * (top_expect + bottom_expect) / img.shape[0]
        bottom_true = top_expect + bottom_expect - top_true
        position_ratio[3] = img.shape[0] / (top_expect + bottom_expect)

    min_pad = max_value
    min_index = 0
    for index in range(len(position_ratio)):
        if position_ratio[index] < min_pad:
            min_index = index
            min_pad = position_ratio[index]

    x_value = middle_x - min_pad * left;
    w_value = min_pad * left + min_pad * right

    if min_index < 3:
        y_value = middle_y - min_pad * top_true
        h_value = min_pad * top_true + min_pad * bottom_true
    elif min_index == 3:
        y_value = middle_y - min_pad * top_true
        h_value = min_pad * top_true + min_pad * bottom_true

    width = 540
    height = 720
    #####



    img = img[int(y_value):int(y_value + h_value), int(x_value):int(x_value + w_value)]

    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)

    filename = os.path.basename(path)

    output = os.path.join("/tmp/thumbnail", filename)

    cv2.imwrite(output, img)


def main():
    for path in sys.argv[1:]:
        img = cv2.imread(path)
        if img is None:
            return
        print(path)
        algorithm2(path, img)


if __name__ == "__main__":
    main()
