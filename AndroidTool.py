import os

cmd_base = "adb shell input tap "

def do(cmd):
    print(cmd)
    os.system(cmd)

def capture_screen(path_and_file_name):   # 捕获获屏幕./T.png path(str)
    do('adb shell screencap -p /sdcard/T.png')
    do('adb pull sdcard/T.png '+path_and_file_name)

def click_on(px,py):    # 点击屏幕  px是屏幕的横坐标 py是屏幕的纵坐标
    cmd = cmd_base + str(px) + " " + str(py)
    do(cmd)




