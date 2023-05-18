import pyautogui
from sleep import SLEEP


pyautogui.PAUSE = 1

def send_message():
    # Entrar no whatsapp web
    pyautogui.click(x=821, y=65)
    SLEEP(1)
    pyautogui.click(x=821, y=65)    
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write('https://web.whatsapp.com')
    pyautogui.press('enter')
    SLEEP(8)

    # Clicar na opção de pesquisar contato e pesquisar
    pyautogui.click(x=430, y=256)
    pyautogui.write('Vitoo')

    # Clicar no contato
    # Clicar no chat

    pyautogui.press('enter')
    # Escrever a mensagem 

    pyautogui.hotkey('ctrl', 'v')
    # Enviar
    pyautogui.press('enter')
