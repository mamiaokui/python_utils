import cv2
import numpy as np


video_path1 = "/Users/mamk/Documents/base.mp4"
cv2.namedWindow("image")
cap1 = cv2.VideoCapture(video_path1)
count1 = 0

fps1 = cap1.get(cv2.CAP_PROP_FPS)
size1 = (int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)))

video_path2 = "/Users/mamk/Documents/mask2.mp4"
cap2 = cv2.VideoCapture(video_path2)
count2 = 0

fps2 = cap1.get(cv2.CAP_PROP_FPS)
size2 = (int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)))


videoWriter = cv2.VideoWriter('merge.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps1, (size1[0]*2, size1[1]))

if fps1 != fps2:
    exit(0)

if size1 != size2:
    exit(0)

success1 = True
success2 = True
count1 = 0;
count2 = 0;

def read_one_frame():
    global success1
    global success2
    if cap1.isOpened() and success1:
        global count1
        count1 += 1
        success1, frame1 = cap1.read()
    if cap2.isOpened() and success2:
        global count2
        count2 += 1
        success2, frame2 = cap2.read()

    if success1 and success2:
        result = np.ndarray(shape=(size1[0], size1[1] * 2, 3), dtype=np.uint8)
        result[0:size1[0], 0:size1[1]] = frame1
        result[0:size1[0], size1[1]:] = frame2
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
