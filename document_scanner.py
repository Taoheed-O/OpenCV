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



# image preprocessing function
def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    imgDil = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDil, kernel, iterations=1)
    
    return imgThres



# get contour function
def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if (area > maxArea) and (len(approx) == 4):
                biggest = approx
                maxArea = area

    return biggest



def getWarp(img, biggest):
    pass



# cam view loop
while True:
    check, img = cam.read()
    img = cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()
    imgThres = preProcessing(img)
    biggest = getContours(imgThres)
    print(biggest)
    getWarp(img, biggest)
    cv2.imshow('img', imgContour)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break



cam.release()
cv2.destroyAllWindows()