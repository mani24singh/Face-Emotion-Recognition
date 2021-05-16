from facial_emotion_recognition import EmotionRecognition

import cv2 as cv

er = EmotionRecognition(device='cpu')

cam = cv.VideoCapture(1)

while True:
    success, frame = cam.read()
    frame = er.rcognise_emotion(frame, return_type='BGR')
    cv.imshow('frame',frme)
    key = cv.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destrroyAllWindows()

