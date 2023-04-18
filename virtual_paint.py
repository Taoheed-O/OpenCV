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


myColorValues = [
    [51, 153, 255],  # B G R          values for  yellow
    [255, 0, 255],  # B G R          values for  purple/magenta
    [0, 255, 0]   # B G R          values for  green
]


# color finding function 
def find_color(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask  = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
        count+=1
        # cv2.imshow(str(color[0]), mask)


# get contour function
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y   

# cam view loop
while True:
    check, img = cam.read()
    imgResult = img.copy()
    find_color(img, myColors, myColorValues)
    cv2.imshow('video', imgResult)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


