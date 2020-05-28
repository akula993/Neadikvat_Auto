import pyautogui			
import time
#currentMouseX, currentMouseY =  pyautogui.position ()
x = int(input('Введите первое значение X: '))#
y = int(input('Введите второе значение Y: '))#

x1 = int(input('Введите третие значение X: '))#
y1 = int(input('Введите четвертое значение Y: '))#

pyautogui.click(x,y,duration=1)# Клик левой клавишой мышки

pyautogui.rightClick(x1,y1,duration=1)# Клик правой клавишой мышки
from tkinter import *

root = Tk()
root.title("Моя первая графическая программа на Python")
root.geometry("400x250")
root.resizable(width=False, height=False)

root.mainloop()
