import pyautogui
from sleep import SLEEP


pyautogui.PAUSE = 1

def send_message(message):
    # Entrar no whatsapp web
    pyautogui.click(x=1777, y=20)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write('https://web.whatsapp.com')
    pyautogui.press('enter')
    SLEEP(8)

    # Clicar na opção de pesquisar contato e pesquisar
    pyautogui.click(x=430, y=256)
    pyautogui.write('Dede')

    # Clicar no contato
    # Clicar no chat

    pyautogui.press('enter')
    # Escrever a mensagem 

    pyautogui.write('{}'.format(message))
    # Enviar
    pyautogui.press('enter')

send_message()