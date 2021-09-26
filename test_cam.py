import cv2
import numpy as np
import sys

idx = sys.argv[1]
print('camera idx: ', idx)

# Get a reference to webcam #0 (the default one)
count = 0
video_capture = cv2.VideoCapture(int(idx))


W, H = 1024, 588

#video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, W)
#video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, H)
#video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
video_capture.set(cv2.CAP_PROP_FPS, 30)


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    print('frame %d, shape' % count, frame.shape)
    count += 1
    #rgb_frame = frame[:, :, ::-1]
    if ret:
        cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()



