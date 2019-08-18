import face_recognition
import cv2
import sys
import os

if __name__ == "__main__":
    for path in sys.argv[1:]:
        img = cv2.imread(path)
        if img is None:
            exit(0)

        face_rects = face_recognition.face_locations(img)

        face_index = None
        x, y, w, h = 0,0,0,0
        if len(face_rects) > 0:
            max_size = 0
            for face_rect in face_rects:
                x, y, w, h = face_rect[3],face_rect[0], face_rect[1]-face_rect[3], face_rect[2]-face_rect[0]
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
        middle_x = x + w/2
        middle_y = y + h/2

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
        ####





        # left_pad = x  /left
        # right_pad = (img.shape[1] - x - w) / right;
        # up_pad = y / top
        # bottom_pad = (img.shape[0] - y - h) / bottom;
        #
        # min_pad = min(left_pad, right_pad, up_pad, bottom_pad)
        #
        # x_value = x - min_pad * left;
        # y_value = y - min_pad * top
        # w_value = min_pad * left + w + min_pad * right
        # h_value = min_pad * top + h + min_pad * bottom
        #
        # img = img[int(y_value):int(y_value + h_value), int(x_value):int(x_value + w_value)]
        #
        # img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
        #
        # filename = os.path.basename(path)
        #
        # output = os.path.join("/tmp/thumbnail", filename)
        #
        # cv2.imwrite(output, img)