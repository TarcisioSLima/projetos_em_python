import random as escolhe_ai
import time as tempinho
import pyautogui as progama # type: ignore

progama.PAUSE = 0.3
vetor = [1,2,3,4,5,6,7,8]

indice = escolhe_ai.randint(0,5)
numero_sorteado = vetor[indice]
print(numero_sorteado)