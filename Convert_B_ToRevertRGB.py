import cv2

video_path = "/Users/mamk/Documents/mask.mp4"
cv2.namedWindow("image")
cap = cv2.VideoCapture(video_path)
count = 0

fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter('oto_other.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, size)


success = True
while cap.isOpened() and success:
    count += 1
    success, frame = cap.read()
    if success:
        if count == 100 or True:
            for i in range (0, frame.shape[0]):
                for j in range (0, frame.shape[1]):
                    rgb = frame[i][j]
                    b = 255 - rgb[0]
                    frame[i][j][0] = b
                    frame[i][j][1] = b
                    frame[i][j][2] = b
        videoWriter.write(frame)
        print(count)
        #cv2.imwrite("%s%s_%d.png" % (output_path, video_name, count), frame)
videoWriter.release()