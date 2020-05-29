import pyautogui	
import keyboard as key  		

#currentMouseX, currentMouseY = pyautogui.position ()
#x = int(input('Введите первое значение X: '))#
#y = int(input('Введите второе значение Y: '))#



money = int(pyautogui.prompt (text = 'Веди количество: ', title = 'Веди количество: ', default = ''))

start1 = pyautogui.prompt (text = 'Выберите кнопку для запуска', title = 'Выберите кнопку', default = '')# При нажатие на первую кнопку 
pyautogui.alert (text = '2 клика', title = 'нажми Enter', button = 'OK')
dans1 = pyautogui.position () # запоминаются 1 данные
pyautogui.alert (text = 'перетаскивания с того места где была 1 точка', title = 'нажми Enter', button = 'OK')
dans2 = pyautogui.position () # запоминаются 1 данные
pyautogui.alert (text = '1 клик', title = 'жМи СуКа Enter', button = 'OK')
dans3 = pyautogui.position () # запоминаются 1 данные
pyautogui.alert (text = '1 клик', title = 'жМи СуКа Enter', button = 'OK')
dans4 = pyautogui.position () # запоминаются 1 данные


while True:
	if key.is_pressed( start1 ):
		 # создаем переменную money и присваиваем ей значение 10
		while money > 0: # Запускаем цикл
			pyautogui.doubleClick(dans1, duration= 1 )
			pyautogui.dragTo(dans2, duration= 1)
			pyautogui.click(dans3, duration= 1)
			pyautogui.click(dans4, duration= 1)
			money -= 1 # Все еще внутри цикла. Уменьшаем на один переменную money
