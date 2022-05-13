import cv2
import numpy as np
import os
import datetime
import sys


currentFrame = 0
width = 1280
height = 720
FPS = 30
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'avc1')

pin_state = 0

while(True):
    pin_state = input()
    if pin_state:
        cap = cv2.VideoCapture(0)
        video = cv2.VideoWriter('camera_processing//video//output.mp4', fourcc, float(FPS), (width, height))

        current_timestamp = datetime.datetime.now()
        hard_cap = current_timestamp + datetime.timedelta(seconds=3)

        while(pin_state and hard_cap > current_timestamp):
            ret, frame = cap.read()
            if ret == True:
                frame = cv2.flip(frame,1)
                video.write(frame)
                cv2.imshow('frame',frame)
            else:
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                pin_state = 0
            current_timestamp = datetime.datetime.now()

        cap.release()
        video.release()
        cv2.destroyAllWindows()
