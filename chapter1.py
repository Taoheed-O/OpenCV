import cv2

print('package imported')
img = cv2.imread('resources/ubuntu.png')
cv2.imshow('output', img)
cv2.waitKey(4000)
