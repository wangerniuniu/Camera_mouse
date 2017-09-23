import cv2#opencv 库
import pyautogui#操作鼠标、键盘库
import  time
cap = cv2.VideoCapture(0)
r_limit=200#RGB三通道阈值，用于提取红色部分
b_limit=150#
g_limit=150#
time.sleep(10)#延时10s启动
while(1):
    # get a frame
    ret, frame = cap.read()#读取图像一帧
    res1 = cv2.resize(frame, None, fx=0.125, fy=0.125, interpolation=cv2.INTER_CUBIC)#图像从640*320缩小至80*60
    b, g, r = cv2.split(res1)#分离RGB三通道的值
    for y in range(0, 80):#遍历80*60的每一个像素
        for x in range(0,60):
            if b[x][y]<b_limit and g[x][y]<g_limit and r[x][y]>r_limit:
                res1[x][y]=(0,0,255)#红色全部用深红色标记
                mouse_x=int(x*20)#电脑显示屏1600*900，图像压缩80*60
                mouse_y=int(y*22.4)
                pyautogui.moveTo(1600-mouse_y, mouse_x, duration=0)#鼠标的位置
                #pyautogui.mouseDown(1600-mouse_y, mouse_x, button='left')
            else:
                res1[x][y]=(255,255,255)#非红色部分用白色代替
                pass
    out = cv2.resize(res1, None, fx=20, fy=22.4, interpolation=cv2.INTER_CUBIC)#扩大图像，80*60 放大至1600*900
    cv2.imshow('capture',out)#显示扩大图像，用于显示
    if cv2.waitKey(1) & 0xFF == ord('q'):#q 跳出循环
        break
    elif cv2.waitKey(1) & 0xFF == ord('a'):# a 截图
        cv2.imwrite('messigray.png', frame)
cap.release()#释放摄像头
cv2.destroyAllWindows()#关闭所有窗口