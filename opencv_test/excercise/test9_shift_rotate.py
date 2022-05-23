import cv2
import numpy as np

canvas = np.zeros( (300,300,3) , dtype='uint8' )

for _ in range (0,25):
# When you are not interested in some values returned by a function we use underscore in place of variable name 
# Basically it means you are not interested in how many times the loop is run till now just that it should run some specific number of times overall.

    radius = np.random.randint(5,200)
    color = np.random.randint(0,256,size=(3,)).tolist()
    # tolist() 將矩陣或一組數字轉變成list
    pt = np.random.randint(0,200,size=(2,))

    cv2.circle(canvas,tuple(pt),radius,color,-1)


cv2.imshow("canvas",canvas)
cv2.waitKey(0)

# Creating a translation matrix = TM

# Negative values for  t_x value will shift the image to the left
# Positive values for  t_x shifts the image to the right

# Negative values for  t_y shifts the image up
# Positive values for  t_y will shift the image down

# 最後圖片結果，也就是往右移動25，往下移動50
# [1,0,25] 表示向[1,0]方向移動25個pixels，[0,1,50] 表示向[0,1]反方向移動25個pixels
TM = np.float32([[1,0,25],[0,1,50]])

# img_translation = cv2.warpAffine(img, translation_matrix, (num_cols , num_rows))
# 要注意，在x軸的移動，是cols的移動，y軸的移動則是rows的移動
shifted_canvas = cv2.warpAffine(canvas,TM,(canvas.shape[1] , canvas.shape[0]) )

cv2.imshow("shifted canvas",shifted_canvas)
cv2.waitKey(0)

# rotate
(h,w) = canvas.shape[:2]
center = (w//2 , h//2)

# (center, 135 , 1.0) 第一個是固定的點，第二個是旋轉角度，第三個是縮放尺度
RM = cv2.getRotationMatrix2D(center, 135 , 1.0)
rotated_canvas = cv2.warpAffine(canvas,RM,(w,h))

cv2.imshow("rotated canvas",rotated_canvas)
cv2.waitKey(0)

# reference :
# https://stackoverflow.com/questions/54274185/shifting-an-image-by-x-pixels-to-left-while-maintaining-the-original-shape
# 