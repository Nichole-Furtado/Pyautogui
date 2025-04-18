import pyautogui as posicao

# = pressionar as teclas do teclado
#windows + r
posicao.hotkey('win', 'r')

posicao.sleep(2)

posicao.typewrite('notepad')

posicao.sleep(2)

posicao.press('enter')

posicao.sleep(2)

posicao.typewrite('Realizando a abertura do bloco de notas :)')

posicao.sleep(2)

fechar = posicao.getActiveWindow()

fechar.close()

posicao.press('tab')

posicao.press('enter')

print('Automação realizada com sucesso!')
