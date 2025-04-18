import pyautogui as mouse
import pyautogui as espera

mouse.sleep(2)
mouse.moveTo(x= 717, y=1174) #verificar a posição da janela do windows, utilizando a função position e print
mouse.sleep(2)
mouse.click(x= 717, y=1174)
mouse.sleep(2)
mouse.typewrite('Google Chrome')
mouse.press('enter')
mouse.sleep(2)
mouse.press('tab')
mouse.press('enter')
mouse.sleep(2)
mouse.typewrite('Valor do Dolar hoje')
mouse.press('enter')