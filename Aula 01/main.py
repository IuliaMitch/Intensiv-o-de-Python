##instalar wheel, para poder instalar pyautogui

# Passo 1: Acessar o sistema da empresa

# Passo 2: Fazer login no sistema

# Passo 3: Baixar a base de dados

# Passo 4: Caulcular os indicadores

# Passo 5: Enviar o email para a diretoria/para o chefe
# https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema
import pyautogui 

pyautogui.PAUSE = 1
#print(pyautogui.__file__)

# 1696, 18
#pyautogui.click => clicar com o mouse
#pyautogui.write => escrever um texto
#pyautogui.press => pressionar uma tecla
#pyautogui.hotkey => apertar uma combinação de teclas
pyautogui.click(x=1697, y=18)
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press(keys='enter')
print('Aguardando web...')
pyautogui.sleep(2)
pyautogui.click(x=1032, y=471)
pyautogui.write('IuliaMitch')
pyautogui.press('tab')
pyautogui.write('iulialinda')
#pyautogui.press('enter')