import cv2
import numpy as np

img = np.zeros((600, 600, 3), np.uint8)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 8)
# cv2.line(影像, 開始座標, 結束座標, 顏色, 線條寬度)
# 在圖像上畫線
# img.shape[0] = 600 、 img.shape[1] = 600 、 img.shape[2] = 3

cv2.rectangle(img, (0, 0), (400, 300), (0, 0, 255), cv2.FILLED)
# cv2.rectangle(影像, 頂點座標, 對向頂點座標, 顏色, 線條寬度)

cv2.circle(img, (300, 400), 30, (255, 0, 0), cv2.FILLED)
# cv2.circle(影像, 圓心座標, 半徑, 顏色, 線條寬度)
# 線條寬度用負值，則會變成實心，也可以用函式來表示

cv2.ellipse(img, (500, 200), (25, 55), 45, 0, 360, (0, 0, 255), 5)
# cv2.ellipse(影像, 中心座標, 軸長, 旋轉角度, 起始角度, 結束角度, 顏色, 線條寬度)

cv2.putText(img, 'Eris', (100, 500), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2 , cv2.LINE_AA )
# cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
# 線條種類可以省略不寫，預設值為cv2.LINE_8，也可以設定反鋸齒的線條效果:cv2.LINE_AA

cv2.imshow('img', img)
cv2.waitKey(0)