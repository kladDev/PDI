import cv2
import numpy as np
img = cv2.imread('ifma.jpg')

cv2.imshow('IFMA', img)

fator = 8

height = img.shape[0] // fator
width = img.shape[1] // fator

new_img = cv2.resize(img, (width, height))

cv2.imwrite('ifma_01.jpg', new_img)

cv2.imshow('IFMA - 02', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()