import cv2 
import numpy as np

# webcam

# defining frame's width and height
widthImg = 640
heightImg = 480

# camera initialization
cam = cv2.VideoCapture(0)

# cam settings
cam.set(3, widthImg)
cam.set(4, heightImg)
cam.set(10, 150)



#defining a kernel -- an array of ones with size 5x5 
kernel = np.ones((5,5))


def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    imgDil = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDil, kernel, iterations=1)
    
    return imgThres



# cam view loop
while True:
    check, img = cam.read()
    img = cv2.resize(img, (widthImg, heightImg))
    cv2.imshow('img', img)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()