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
myColors = [[5, 107, 0, 19, 255, 255],
            [133, 56, 0, 159, 156, 255],
            [57, 76, 0, 100, 255, 255]]


# color finding function 
def find_color(img, myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask  = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow(str(color[0]), mask)



# cam view loop
while True:
    check, frame = cam.read()
    find_color(frame, myColors)
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


