import cv2
lena = cv2.imread("lena.bmp")
r = cv2.imwrite("result.bmp",lena)

# retval = cv2.imwrite( filename, img[, params])
# retval : 回傳值，儲存成功回傳True，儲存失敗回傳False
# filename : 儲存結果的檔案名
# img : 被儲存影像的名稱
# params : 儲存類型參數

# 先讀取lena.bmp的影像，產生它的備份影像
# 再以result.bmp儲存到左邊目錄