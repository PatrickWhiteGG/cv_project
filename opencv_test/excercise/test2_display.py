import cv2
lena = cv2.imread("C:/Users/Roy/Desktop/Programming/opencv_test/photo/lena.bmp",1)
print(lena)
# from test1

cv2.namedWindow("window")
# namedWindow語法為 : None = cv2.namedWindow ( winname )
# 建立指定名稱的視窗的語法
# winname : 所要建立視窗的名稱

cv2.imshow("window",lena)
# None = cv2.imshow(winname , mat)
# winname : 視窗名稱
# mat : 要顯示的影像

retval=cv2.waitKey()
# 讓圖片不會一閃而過的語法
# retval=cv2.waitKey( [delay] )
# 也可以直接cv2.waitKey(0)
