import cv2
def fun():
    cap = cv2.VideoCapture("/tmp/test.mp4")
    count = 0

    success = True
    while cap.isOpened() and success:

        success, frame = cap.read()
        if success:
            count += 1
            crop = frame[0:frame.shape[0], frame.shape[1]/2:frame.shape[1]]
            cv2.namedWindow("a")
            cv2.imshow("a", crop)
            if count > 100:
                cv2.waitKey(0)

            lt = [1000000, 1000000]
            rt = [-1, 1000000]
            lb = [1000000, -1]
            rb = [-1, -1]
            if count > 100:
                for i in range(0, crop.shape[0]):
                    for j in range(0, crop.shape[1]):
                        if crop[i][j][0] < 250:
                            if lt[0] > i and lt[1] > j:
                                lt[0] = i
                                lt[1] = j
                            if rt[0] < i and rt[1] > j:
                                rt[0] = i
                                rt[1] = j
                            if lb[0] > i and lb[1] < j:
                                lb[0] = i
                                lb[1] = j
                            if rb[0] < i and rb[1] < j:
                                rb[0] = i
                                rb[1] = j

                print(lt)
                print(rt)
                print(lb)
                print(rb)




    print(count)

fun()