import cv2

# print('package imported')
# img = cv2.imread('resources/images/ubuntu.png')
# cv2.imshow('output', img)
# cv2.waitKey(4000)

cap = cv2.VideoCapture('resources/videos/baby.mp4')
while True:
    success, img = cap.read()
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
