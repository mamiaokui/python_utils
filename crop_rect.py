import numpy as np
import cv2
import sys
import os

watermark_flag = True
if __name__ == "__main__":
    path = sys.argv[1]
    cap = cv2.VideoCapture(path)
    file_name_without_suffix = os.path.basename(path).split(".")[0]
    width = int(cap.get(3))
    height = int(cap.get(4))
    framerate = int(cap.get(5))
    framenum = int(cap.get(7))

    video = np.zeros((framenum, height, width, 3), dtype='float16')
    watermark_width = width / 3
    watermark_height = watermark_width / 2
    watermark_size = max(watermark_width, watermark_height)
    watermark_width = watermark_size
    watermark_height = watermark_size

    cnt = 0
    success = True
    while cap.isOpened() and success:
        success, frame = cap.read()
        if success:
            cnt += 1
            watermark = frame
            if watermark_flag:
                watermark = frame[0:watermark_height, 0:watermark_width]
            else:
                watermark = frame[watermark_height+10:2*watermark_height+10, watermark_width+10:2*watermark_width+10]
            sub_path = "/crop_yes"
            if not watermark_flag:
                sub_path = "/crop_no"

            watermark = cv2.resize(watermark, (64, 64))
            cv2.imwrite("%s/%s_%d.jpg" % (os.path.dirname(path) + sub_path, file_name_without_suffix, cnt), watermark)

    print("end")


