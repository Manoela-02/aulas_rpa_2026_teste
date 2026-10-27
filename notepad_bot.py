import time
import pyautogui


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

def main():
    print("Iniciando a automação do Bloco de Notas...")


    pyautogui.press('win')
    time.sleep(1.0)


    pyautogui.write('notepad', interval=0.1)
    pyautogui.press('enter')


    time.sleep(2.0)


    texto = "Relatório de Execução Automática - RPA PyAutoGUI Ativo!"
    pyautogui.write(texto, interval=0.05)


    pyautogui.hotkey('ctrl', 's')
    time.sleep(1.0)

    pyautogui.write('status_bot.txt', interval=0.1)
    pyautogui.press('enter')

    print("Automação concluída e arquivo salvo com sucesso!")

if __name__ == "__main__":
    main()