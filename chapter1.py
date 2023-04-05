import cv2

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

img =  cv2.imread('resources/images/ubuntu.png')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', imgGray)
cv2.waitKey(0)