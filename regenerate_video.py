import cv2
import numpy as np


video_path1 = "/Users/mamk/Desktop/a.mp4"
cv2.namedWindow("image")
cap1 = cv2.VideoCapture(video_path1)
count1 = 0

fps1 = cap1.get(cv2.CAP_PROP_FPS)
size1 = (int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)))



videoWriter = cv2.VideoWriter('merge.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps1, (size1[0], size1[1]))


success1 = True
count1 = 0

def read_one_frame():
    global success1
    if cap1.isOpened() and success1:
        global count1
        count1 += 1
        success1, frame1 = cap1.read()


    if success1:
        result = np.ndarray(shape=(size1[1], size1[0], 3), dtype=np.uint8)
        result[0:size1[1], 0:size1[0]] = frame1
        #cv2.imshow("image", result)
        #cv2.waitKey(0)
        return result

    return None


while success1:
    frame = read_one_frame()
    if frame is not None:
        videoWriter.write(frame)
        print(count1)
    else:
        break
videoWriter.release()
