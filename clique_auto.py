import pyautogui
import time

time.sleep(5)


x, y = 520, 306
z, w = 244, 255
x1, y2 = 230, 203
#a, b = 630, 800
a, b = 540, 840
c, d = 340, 840
e, f = 1813, 169
g, h = 975, 235
clicks=0
try:
    while True:
        
        #pyautogui.hotkey('ctrl', 'v')
        #time.sleep(5)
        pyautogui.doubleClick(x, y)
        time.sleep(2) 
        pyautogui.click(z, w)  
        time.sleep(2)  
        pyautogui.click(a, b, clicks=3)
        time.sleep(2)
        pyautogui.typewrite('581')
        #pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.click(c, d)
        time.sleep(1)
        pyautogui.click(x1, y2)
        time.sleep(2)
        pyautogui.click(e, f)
        time.sleep(2)
        y+=30
        clicks+=1
        if clicks==2:
           # break
            pyautogui.click(g, h)
            time.sleep(2)
            y=306
except KeyboardInterrupt:
    print("Automação interrompida.")