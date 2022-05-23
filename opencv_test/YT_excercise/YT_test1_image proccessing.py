import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

kernel1 = np.ones((5, 5), np.uint8)

img = cv2.imread('C:/Users/Roy/Desktop/Programming/opencv_test/photo/colorcolor.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]] )

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 轉換顏色，由RGB轉到灰階，將圖像從一個顏色空間轉換到另一個顏色空間
# 在做圖像處理時，常常需要用到灰階圖、二值圖、HSV、HSI等格式
# 利用這個函式，便能將RGB圖像轉成以上幾種

blur = cv2.GaussianBlur(img, (15, 15), 10)
# 高斯模糊，去雜訊，(15,15)是Gaussian kernel size，10則是標準差

canny = cv2.Canny(img, 200, 250)
# 影像邊緣偵測，200是指定門檻值 threshold1，250是指定門檻值 threshold2
# first threshold for the hysteresis procedure ， second threshold for the hysteresis procedure

dilate = cv2.dilate(canny, kernel, iterations=1)
# 影像膨脹，常常會先用erode侵蝕的方式讓線條變窄、去噪
# 再利用dilate膨脹，把影像給加寬回來

erode = cv2.erode(dilate, kernel1, iterations=1)
# 影像侵蝕，對於影像的去噪很有幫助，像是移除影像中的小白雜點、雜訊


cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)