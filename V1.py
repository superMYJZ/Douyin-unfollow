#-*-coding:utf-8-*-
import AndroidTool
import cv2
import findText
from PIL import Image

file_p = './T.png'
click_x_center = (1040 + 870) / 2		#已关注按键的横向最中间 需自行测量

def picture_ready(screen_high,need_left,need_right):		# 以下参数自行测量 screen_high是屏幕分辨率的高度,need_left抖音已关注按键的最左端,need_right抖音已关注按键的最右端 若是无法识别文字可适当加大左右距离

    AndroidTool.capture_screen(file_p)
    img = cv2.imread(file_p)
    img = img[0:screen_high,need_left:need_right ]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite("./T.png", img)


def roll_page(): #抖音极速版
    AndroidTool.do('adb shell input swipe 540 2000 540 540 500')
    AndroidTool.do('adb shell input swipe 540 1140 540 1170 200')

def main():

    while True:
        roll_page()


        picture_ready(2280,820,1040)
        im = Image.open('./T.png')
        img = cv2.imread('./T.png')

        need_click= findText.detect(img,im)
        print(need_click)
        print(len(need_click))

        if len(need_click)==0:
            exit(-1)

        for every_need in need_click:
            AndroidTool.click_on((1040+870)/2,every_need)


if __name__ == '__main__':
    main()
