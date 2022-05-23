import cv2
lena = cv2.imread("lena.bmp")
cv2.imshow("demo",lena)
key = cv2.waitKey()

if key == ord('A'):
    cv2.imshow("PressA",lena) # 互動式，輸入大寫A，就會跳出PressA的視窗
    retval=cv2.waitKey()      # 留住新視窗
elif key == ord('B'):
    cv2.imshow("PressB",lena) # 同上
    retval=cv2.waitKey()
