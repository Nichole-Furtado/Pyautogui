import pyautogui as escolha

opcao = escolha.confirm('Clique no botão desejado',
        buttons = ['Excel', 'Word','Notepad'])

if opcao == "Excel":
    escolha.hotkey('win', 'r')
    escolha.write('Excel')
    escolha.press('enter')
    escolha.sleep(3)
    escolha.press('enter')
    escolha.write('Voce escolheu Excel :)')
    print(" Você escolheu Excel")

elif opcao == "Word":
    escolha.hotkey('win', 'r')
    escolha.write('winword')
    escolha.press('enter')
    escolha.sleep(3)
    escolha.press('enter')
    escolha.write('Voce escolheu Word :)')
    print(" Você escolheu Word")
    print("Você escolheu Word")

else:
    escolha.hotkey('win', 'r')
    escolha.write('notepad')
    escolha.press('enter')
    escolha.sleep(3)
    escolha.press('enter')
    escolha.write('Voce escolheu Notepad :)')
    print("Você escolheu Notepad")

