import cv2
import numpy as np
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


img = cv2.imread('resources/images/linux_mint_logo.png')
print(img.shape)

imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow('Image', img)
cv2.imshow('Image Resize', imgResize)
cv2.imshow('Image crop',imgCropped)

cv2.waitKey(0)