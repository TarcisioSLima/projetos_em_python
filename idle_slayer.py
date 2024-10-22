import time
import pyautogui # type: ignore

pyautogui.PAUSE = 0.3

#abrir Idle Slayer + Steam
pyautogui.press("win")
pyautogui.write("idle")
pyautogui.press("enter")
time.sleep(15)

#Desativando Janela de permição Segurança Steam
pyautogui.FAILSAFE

#Escolhendo o Usuário
pyautogui.click(x=811, y=583)
time.sleep(18)

#entrando no jogo
pyautogui.click(x=1120, y=759)
time.sleep(8)
pyautogui.press('enter')
time.sleep(5)

#Colentando os bonus e Enviando os Vassalos
pyautogui.click(x=1162, y=16)
pyautogui.click(x=893, y=11)
pyautogui.click(x=144, y=101)

pyautogui.click(x=459, y=975)

pyautogui.click(x=674, y=220)
pyautogui.click(x=674, y=220)
pyautogui.click(x=674, y=220)
pyautogui.click(x=658, y=479)
pyautogui.click(x=658, y=479)
pyautogui.click(x=650, y=716)
pyautogui.click(x=650, y=716)
pyautogui.click(x=616, y=892)
pyautogui.click(x=616, y=892)

#Saindo do jogo
pyautogui.press('esc')
pyautogui.press('esc')
pyautogui.click(x=807, y=816)
time.sleep(2)

#Desativando Steam
pyautogui.press('win')
time.sleep(1)
pyautogui.click(x=1472, y=1040)
time.sleep(2)

pyautogui.click(x=1587, y=943)

time.sleep(2)

pyautogui.click(x=1663, y=936)

print("Os bonus de Idle Slayer foram coletados :)")
#_________________________________________________________________________________________
#                                  Idle Slayer Encerrado
#_________________________________________________________________________________________
print("Todas as tarefas foram concluidas!!")