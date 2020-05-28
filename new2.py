import pyautogui			
# importtime
#currentMouseX, currentMouseY = pyautogui.position ()
#x = int(input('Введите первое значение X: '))#
#y = int(input('Введите второе значение Y: '))#

#x1 = int(input('Введите третие значение X: '))#
#y1 = int(input('Введите четвертое значение Y: '))#
import datetime
import keyboard

def check_state(cur_time=datetime.datetime.now()) -> None:
    new_time = cur_time + datetime.timedelta(seconds=10)
    print("Для продолжения нажмите Enter...")
    while datetime.datetime.now() < new_time:
        if keyboard.is_pressed('Enter'):
            q = pyautogui.position ()
            print(q)    
    else:
        print("timeout")

check_state()
 
check_state()
#q = pyautogui.position ()
#print(q)
#x1 = currentMouseX, currentMouseY
#click1 = pyautogui.click(x1+100, duration=1)# Клик левой клавишой мышки
#x2 = currentMouseX, currentMouseY
#click2 = pyautogui.doubleclik(x2, duration=1)# Клик левой клавишой мышки# Клик правой клавишой мышки
#from  tkinterimport *

#root = Tk()
#root.title("Моя первая графическая программа на Python")
#root.geometry("400x250")
#root.resizable(width= False, height= False)

#root.mainloop()
