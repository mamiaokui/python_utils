import cv2
import sys
import os


def add_cover(image_video, image_cover):

    image_video = cv2.resize(image_video, (64, 64))
    if image_cover is None:
        return image_video

    w = image_video.shape[1]
    h = image_video.shape[0]
    image_cover = cv2.resize(image_cover, (w, h), interpolation=cv2.INTER_NEAREST)
    image_result = image_video.copy()

    for i in range(h):
        for j in range(w):
            pixel = image_cover[i][j]
            if pixel[0] != 0 and pixel[1] != 0 and pixel[2] != 0:
                image_result[i][j] = pixel
            else:
                image_result[i][j] = image_video[i][j] * 0.5
    return image_result


def process(video_path, cover_path, output_path):
    cap = cv2.VideoCapture(video_path)
    count = 0
    if os.path.exists(cover_path):
        image_cover = cv2.imread(cover_path)
    else:
        image_cover = None

    video_name = os.path.basename(video_path)

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    success = True
    while cap.isOpened() and success:
        count += 1
        success, frame = cap.read()
        if success:
            frame = add_cover(frame, image_cover)
            cv2.imwrite("%s%s_%d.png" % (output_path, video_name, count), frame)

def process_with_cover():
    arr = ["/Users/mamk/Downloads/vmate_video/no_tail/a60qykk6zn2_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/a80co9da4nb_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/adbc3ppakv0_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/akkvmbyysk9_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/aoa5ddh9ypn_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/atqmc4g0gw0_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/ax4pnkcp3cy_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/azkomri33ab_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/a7choofrma7_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/a9wr2nc4qb8_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/ae532hampcl_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/alltmwyzcc6_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/aop83s1ee5c_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/atrqiuvbmfg_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/axwi71fbl3u_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/i1jzy8n1aqk_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/a7f77saojlh_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/abdjmozgyhb_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/afwspl3xssv_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/am00l9lkka2_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/aounwbbf364_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/avxjo2x4a8p_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/ayunwo83bve_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/a7jiym6b1e0_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/ac4jhe1w9qm_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/ahhg5ispmx9_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/anthfzgez8g_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/apht4zp4ep5_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/aw9d2y3i769_NEW.mp4", \
    "/Users/mamk/Downloads/vmate_video/no_tail/az5hxibcdzm_NEW.mp4"]

    for i in arr:
        print(i)
        process(i, "/Users/mamk/Documents/cover.png", "/tmp/b/yes/")
    print("finish with cover")


def process_without_cover():
    arr = ["/Users/mamk/Downloads/vmate_video/no_tail/a60qykk6zn2_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/a80co9da4nb_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/adbc3ppakv0_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/akkvmbyysk9_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/aoa5ddh9ypn_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/atqmc4g0gw0_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/ax4pnkcp3cy_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/azkomri33ab_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/a7choofrma7_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/a9wr2nc4qb8_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/ae532hampcl_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/alltmwyzcc6_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/aop83s1ee5c_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/atrqiuvbmfg_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/axwi71fbl3u_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/i1jzy8n1aqk_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/a7f77saojlh_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/abdjmozgyhb_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/afwspl3xssv_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/am00l9lkka2_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/aounwbbf364_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/avxjo2x4a8p_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/ayunwo83bve_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/a7jiym6b1e0_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/ac4jhe1w9qm_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/ahhg5ispmx9_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/anthfzgez8g_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/apht4zp4ep5_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/aw9d2y3i769_NEW.mp4", \
           "/Users/mamk/Downloads/vmate_video/no_tail/az5hxibcdzm_NEW.mp4"]

    for i in arr:
        print(i)
        process(i, "", "/tmp/b/no/")

    print("finish without cover")


if __name__ == "__main__":
    #process_with_cover()
    process_without_cover()

