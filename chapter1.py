import cv2
import numpy as np


# incomplete function...
# def stackImages(scale, imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range(0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0,0), None,)   



# image
# print('package imported')
# img = cv2.imread('resources/images/ubuntu.png')
# cv2.imshow('output', img)
# cv2.waitKey(4000)

# video
# cap = cv2.VideoCapture('resources/videos/baby.mp4')
# while True:
#     success, img = cap.read()
#     cv2.imshow('video', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# webcam
# cam = cv2.VideoCapture(0)
#
# while True:
#     check, frame = cam.read()
#     cv2.imshow('video', frame)
#     key = cv2.waitKey(1)
#     if key & 0xFF == ord('q'):
#         break
# cam.release()
# cv2.destroyAllWindows()

# color sections
# img =  cv2.imread('resources/images/ubuntu.png')
# kernel = np.ones((5,5), np.uint8)

# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur =  cv2.GaussianBlur(imgGray,(7,7), 0)
# imgCanny = cv2.Canny(img, 100, 100)
# imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

# cv2.imshow('gray', imgGray)
# cv2.imshow('blur', imgBlur)
# cv2.imshow('canny', imgCanny)
# cv2.imshow('Dilation', imgDialation)
# cv2.imshow('Eroded', imgEroded)

# cv2.waitKey(0)

# Resize and cropping
# img = cv2.imread('resources/images/linux_mint_logo.png')
# print(img.shape)

# imgResize = cv2.resize(img, (300, 200))
# print(imgResize.shape)

# imgCropped = img[0:200, 200:500]

# cv2.imshow('Image', img)
# cv2.imshow('Image Resize', imgResize)
# cv2.imshow('Image crop',imgCropped)

# cv2.waitKey(0)


# drawing on images

# img = np.zeros((512, 512,3), np.uint8)

# print(img.shape)
# img[200:500, 100:300] = 255,0,0

# cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)
# cv2.rectangle(img, (0,0), (250, 350),(0,0, 255), 2) #cv2.FILLED)
# cv2.circle(img, (400, 50),30, (255, 255, 0), 5)
# cv2.putText(img, "OpenCV", (300, 200),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,150,0),3)

# cv2.imshow('Image', img)

# cv2.waitKey(0)


# Warp perspective
# img = cv2.imread('resources/images/linux_mint_logo.png')

# width, height = 250,350
# pts1 = np.float32([[111, 219], [287, 188], [154, 482],[352, 440]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width, height]])
# matrix = cv2.getPerspectiveTransform(pts1, pts2)
# imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# cv2.imshow('Image', img)
# cv2.imshow('output', imgOutput)

# cv2.waitKey(0)


# joining Images
# img = cv2.imread('resources/images/linux_mint_logo.png')

# imgHor = np.hstack((img, img))
# imgVert = np.vstack((img, img))

# cv2.imshow('horizontal stack', imgHor)
# cv2.imshow('vertical stack', imgVert)

# cv2.waitKey(0)


# color detection
# def func(a):
#     pass


# path = 'resources/images/linux_mint_logo.png'
# cv2.namedWindow('TrackBars')
# cv2.resizeWindow('TrackBars', 640, 240)


# cv2.createTrackbar('Hue Max', 'TrackBars', 4,179, func)
# cv2.createTrackbar('Hue Min', 'TrackBars', 0,179, func)
# cv2.createTrackbar('Sat Max', 'TrackBars', 255,255, func)
# cv2.createTrackbar('Sat Min', 'TrackBars', 0,255, func)
# cv2.createTrackbar('Val Max', 'TrackBars', 255,255, func)
# cv2.createTrackbar('Val Min', 'TrackBars', 7,255, func)



# while True:
#     img = cv2.imread(path)
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
#     h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
#     sat_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')
#     sat_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')
#     val_max = cv2.getTrackbarPos('Val Max', 'TrackBars')
#     val_min = cv2.getTrackbarPos('Val Min', 'TrackBars')

#     print(h_max, h_min, sat_max, sat_min, val_max, val_min)
#     lower = np.array([h_min, sat_min, val_min])
#     upper = np.array([h_max, sat_max, val_max])
#     mask  = cv2.inRange(imgHSV, lower, upper)

#     imgResult = cv2.bitwise_and(img,img, mask=mask)

#     # show
#     cv2.imshow('original', img)
#     cv2.imshow('hsv',imgHSV)
#     cv2.imshow('mask', mask)
#     cv2.imshow('img Result', imgResult)
#     cv2.waitKey(1)


# contours/ shape detection

# image resize function
def imgResize(img):
    img = cv2.resize(img, (300,300))
    return img

# image contour function
def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255,0,0),3)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3:
                objectType = 'Triangle'
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = 'square'
                else:
                    objectType = 'rectangle'
            elif objCor == 5:
                objectType = 'pentagon'
            elif objCor == 6:
                objectType = 'hexagon'
            elif objCor == 7:
                objectType = 'heptagon'
            elif objCor == 8:
                objectType = 'octagon'
            elif objCor == 9:
                objectType = 'nonagon'
            elif objCor == 10:
                objectType = 'decagon'
            elif objCor > 10:
                objectType = 'circle'
            else:
                objectType = 'unknown'
            
            cv2.rectangle(imgContour, (x,y),(x+w, y+h),(0,255,0), 2)
            cv2.putText(imgContour, objectType, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)






path = 'resources/images/shapes.png'
img = cv2.imread(path)
img = imgResize(img)
imgContour = img.copy()




imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)


cv2.imshow('contour', imgContour)
cv2.imshow('original', img)
cv2.imshow('Gray', img)
cv2.imshow('Blur', imgBlur)
cv2.waitKey(0)