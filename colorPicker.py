import pyautogui
import time

st = time.time()
##############################################

def main():
    startColor = 0
    while True:
        color = colorPick()
        if color != startColor:
            print(color)
            startColor = color

def colorPick():
    x, y = pyautogui.position()
    pixelColor = pyautogui.screenshot().getpixel((x, y))
    return pixelColor
  
main()
    

#############################

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
