##instalar wheel, para poder instalar pyautogui


# https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema
import pyautogui 

pyautogui.PAUSE = 1
#print(pyautogui.__file__)
def SLEEP(self):
    print('Aguardando web...')
    pyautogui.sleep(self)

# 1696, 18
#pyautogui.click => clicar com o mouse
#pyautogui.write => escrever um texto
#pyautogui.press => pressionar uma tecla
#pyautogui.hotkey => apertar uma combinação de teclas


# Passo 1: Acessar o sistema da empresa

pyautogui.click(x=1697, y=18)
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press(keys='enter')
SLEEP(5)

# Passo 2: Fazer login no sistema

pyautogui.click(x=1032, y=471)
pyautogui.write('IuliaMitch')
pyautogui.press('tab')
pyautogui.write('iulialinda')
pyautogui.click( x=1012, y=669)
SLEEP(5)

# Passo 3: Baixar a base de dados

pyautogui.click(x=1372, y=428, button='right')
pyautogui.click(x=1422, y=901)


# Passo 4: Calcular os indicadores

# Passo 5: Enviar o email para a diretoria/para o chefe


