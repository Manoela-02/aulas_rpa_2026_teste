import time
import pandas as pd
import pyautogui


pyautogui.FAILSAFE = True


pyautogui.PAUSE = 0.5


def executar_automacao():
  print("Iniciando o robô de lançamento de notas...")
  print("Você tem 5 segundos para posicionar o cursor e a janela do sistema.")
  time.sleep(5)


  try:
    tabela = pd.read_csv("alunos.csv", sep=";")
  except Exception as e:
    print(f"Erro ao ler o arquivo de dados: {e}")
    return


  for index, aluno in tabela.iterrows():
    ra = str(aluno["RA"])
    nota = str(aluno["Nota01"])

  
    pyautogui.click(x=350, y=200)

 
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")

  
    pyautogui.write(ra)
    pyautogui.press("tab")

  
    pyautogui.write(nota)


    pyautogui.press("enter")


    time.sleep(1.0)

    print(f"Nota do RA {ra} lançada com sucesso!")

  print("Automação concluída! Todas as notas foram processadas.")


if __name__ == "__main__":
  executar_automacao()