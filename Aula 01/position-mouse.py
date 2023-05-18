import pyautogui
pyautogui.sleep(3)

x, y = pyautogui.position()
print('Valor x: {}, e valor y: {}'. format(x,y))