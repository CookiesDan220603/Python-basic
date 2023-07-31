import cv2
import matplotlib.pyplot as plt
img_grayscale = cv2.imread('chokhoi.jpg',0)
cv2.imshow('graycsale image',img_grayscale)
cv2.waitKey(1000000000)