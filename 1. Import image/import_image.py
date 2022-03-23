# import package
import cv2

#import image
image=cv2.imread('Lenna.png')

# show image
cv2.imshow('Lenna',image)
cv2.waitKey()
cv2.destroyWindow()