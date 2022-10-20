import pyautogui
import time

st = time.time()
##############################################

def main():
     while True:
        time.sleep(0.5)
        print(colorPick())

def colorPick():
    x, y = pyautogui.position()
    pixelColor = pyautogui.screenshot().getpixel((x, y))
    return pixelColor
  
main()
    

#############################

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
