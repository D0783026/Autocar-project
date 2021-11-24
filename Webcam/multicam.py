import numpy as np
import cv2

index = 0
arr = []
while True:
    cap = cv2.VideoCapture(index)

    if not cap.read()[0]:
        break
    else:
        arr.append(index)
    cap.release()
    index += 1

video_captures = [cv2.VideoCapture(idx) for idx in arr]

while True:
    # Capture frame-by-frame
    frames = []
    frames_preview = []

    for i in arr:
        # skip webcam capture
        if i == 1: continue
        ret, frame = video_captures[i].read()
        if ret:
            frames.append(frame)
            small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            frames_preview.append(small)

    for i, frame in enumerate(frames_preview):
        cv2.imshow('Cam {}'.format(i), frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
for video_capture in video_captures:
    video_capture.release()
cv2.destroyAllWindows()