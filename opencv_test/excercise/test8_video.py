import cv2

cap = cv2.VideoCapture("thumb.mp4")
# cv2.VideoCapture(filename)
# filename除了可以放檔案名以外，也可以用指定參數 : 0 = 第一隻網路攝影機 , 1 = 第二隻...

while True:
    ret, frame = cap.read()
    # 用read()函式來讀取影像的圖片
    # read()函式會讀取影像中，下一幀的畫面(從頭開始也就是從第一幀圖片開始)
    # read()會傳回來兩個值 :
    # ret : 是否取得圖片(T or F)
    # frame : 圖片
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=1.2, fy=1.2)
        # resize能夠調整視窗大小
        # cv2.resize(image, (256, 256) ) 這樣子是直接調長寬的大小
        # cv2.resize(frame, (0, 0), fx=1.2, fy=1.2) 這樣子是調長寬的倍率
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        # waitKey(10) 也就是每一幀圖片會停留10毫秒，可以藉由這邊數字來控制影片快慢
        # cv2.waitKey(10) == ord('q') 一旦輸入q，就會跳脫while迴圈，影片便會停止
        # waitKey()函式是會接收鍵盤輸入的值，所以用這樣的if函式作判斷，便能夠達到讓影片中斷的效果
        # 順帶一提，若括號內輸入的是零 -> waitKey(0) ， 影片會直接在第一幀停下來
        break