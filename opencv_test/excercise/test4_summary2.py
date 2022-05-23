import cv2
lena = cv2.imread("lena.bmp")
cv2.imshow("demo",lena)
key = cv2.waitKey()
if key != -1 :
    print("觸發了按鍵")

# 在一個視窗內顯示影像，用cv2.waitKey()函式來實現程式的暫停
# 在輸入任意鍵之前，程式會暫停運作
# 當按下任意按鍵後，key = cv2.waitKey()下方的程式才得以繼續執行