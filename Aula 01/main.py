##instalar wheel, para poder instalar pyautogui


# https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema
import pyautogui 
from calculate import calculator
from sleep import SLEEP
from send import send_message 

pyautogui.PAUSE = 1
#print(pyautogui.__file__)


# 1696, 18
#pyautogui.click => clicar com o mouse
#pyautogui.write => escrever um texto
#pyautogui.press => pressionar uma tecla
#pyautogui.hotkey => apertar uma combinação de teclas


# Passo 1: Acessar o sistema da empresa

pyautogui.hotkey('alt', 'tab')
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

#pip install pandas
#pip install openpyxl
#pip install numpy

result = calculator()


# Passo 5: Enviar o email para a diretoria/para o chefe

send_message('Estou enviando uma analise de dados feita por uma automação')
pyautogui.write('Total Gasto: {}'.format(result['total_gasto']))
pyautogui.hotkey('shift', 'enter')
pyautogui.write('Quantidade: {}'.format(result['quantidade']))
pyautogui.hotkey('shift', 'enter')
pyautogui.write('Preco Medio: {}'.format(result['preco_medio']))
pyautogui.hotkey('shift', 'enter')
pyautogui.press('enter')

print('Concluido com sucesso!')