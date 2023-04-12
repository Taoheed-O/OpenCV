import cv2 

# webcam

# defining frame's width and height
frameWidth = 640
frameHeight = 480

cam = cv2.VideoCapture(0)

# cam settings
cam.set(3, frameWidth)
cam.set(4, frameHeight)
cam.set(10, 150)

while True:
    check, frame = cam.read()
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


