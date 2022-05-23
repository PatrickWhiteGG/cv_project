import cv2
lena = cv2.imread("lena.bmp")
cv2.imshow("demo",lena)
cv2.waitKey()
# 當未按下任意按鍵時，程式會暫停在顯示demo視窗
cv2.destroyWindow("demo")
# 當按下任意按鍵後，程式執行，將demo視窗釋放/銷毀