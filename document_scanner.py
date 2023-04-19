import cv2 
import numpy as np

# webcam

# defining frame's width and height
frameWidth = 640
frameHeight = 480

# camera initialization
cam = cv2.VideoCapture(0)

# cam settings
cam.set(3, frameWidth)
cam.set(4, frameHeight)
cam.set(10, 150)








# cam view loop
while True:
    check, img = cam.read()


    cv2.imshow('img', img)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break



cam.release()
cv2.destroyAllWindows()