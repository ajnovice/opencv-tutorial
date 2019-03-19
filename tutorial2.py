import numpy as np
from cv2 import cv2 as cv


def read_saved_video(video_path):
    cap = cv.VideoCapture(video_path)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            # gray = cv.cvtColor(frame, cv.COLOR_BAYER_RG2RGB)
            cv.imshow("frame", frame)
            if cv.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv.destroyAllWindows()


def read_from_camera():
    cap = cv.VideoCapture(0)
    while (cap.isOpened):
        ret, frame = cap.read()
        if ret:
            cv.imshow("frame2", frame)
            if cv.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv.destroyAllWindows()


read_from_camera()
## add video path of you choice and uncomment the the following line
# read_saved_video('Kaggle.mp4')
#
