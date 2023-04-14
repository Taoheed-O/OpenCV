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


# color list
myColors = []


# color finding function 
# def find_color(img):
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     lower = np.array([h_min, sat_min, val_min])
#     upper = np.array([h_max, sat_max, val_max])
#     mask  = cv2.inRange(imgHSV, lower, upper)
#     cv2.imshow('img', mask)



# cam view loop
while True:
    check, frame = cam.read()
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
