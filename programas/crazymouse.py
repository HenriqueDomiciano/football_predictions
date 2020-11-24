import pyautogui
import random
import time

def move_and_click():
    a=0
    valx,valy=pyautogui.size()
    value=pyautogui.confirm(text='Really?',title='Really?',buttons=['ok','Cancel']) 
    if value=='ok':
        while True: 
            x=random.randint(0,valx)
            y=random.randint(0,valy)
            pyautogui.moveTo(x,y)
            pyautogui.click(button='right')
            a=a+1
            if a==2000:
                break
    else :
        pass
move_and_click()