#_________________________________________________________________________________________
#                                       Imports
#_________________________________________________________________________________________
import time
import pyautogui # type: ignore
import random
print("Iniciando Tarefas")
#_________________________________________________________________________________________
#                               Pesquisa no Edge Incio
#_________________________________________________________________________________________

print("'Pesquisa no Edge' em Execução :)")

pyautogui.PAUSE = 0.3

palavras = [

    ['suco', 'chá', 'computador', 'viagem', 'árvore', 'amarelo', 'cidade', 'salgados', 'marron', 'montanha', 'navio', 'papel', 'chuva', 'fogo', 'caderno', 'porta', 'amigo', 'ceia', 'avião', 'bicicleta', 'gato', 'helicóptero', 'aluno', 'casa', 'fruta', 'nuvem', 'azul', 'rosa', 'vermelho', 'sapato'],

    ['casa', 'porta', 'praia', 'gato', 'fogo', 'camisa', 'helicóptero', 'viagem', 'ouro', 'doces', 'mesa', 'carro', 'flor', 'suco', 'cinza', 'cidade', 'almoço', 'café', 'aluno', 'telefone', 'ceia', 'ferro', 'amigo', 'computador', 'arco', 'moto', 'lua', 'livro', 'montanha', 'navio'],

    ['telefone', 'verde', 'estrada', 'professor', 'prata', 'flor', 'doces', 'almoço', 'sapato', 'branco', 'céu', 'ceia', 'mesa', 'aluno', 'vermelho', 'jantar', 'íris', 'salgados', 'suco', 'janela', 'cidade', 'ouro', 'camisa', 'amigo', 'escola', 'fruta', 'lápis', 'praia', 'moto', 'chá'],

    ['suco', 'doces', 'tempo', 'neve', 'caderno', 'gato', 'marron', 'moto', 'escola', 'azul', 'amigo', 'prata', 'almoço', 'viagem', 'céu', 'fogo', 'papel', 'caneta', 'bola', 'cinza', 'jantar', 'arco', 'sol', 'rosa', 'salgados', 'flor', 'carro', 'camisa', 'livro', 'professor'],

    ['caneta', 'íris', 'jantar', 'moto', 'lua', 'camisa', 'viagem', 'diamante', 'cinza', 'caderno', 'amigo', 'sol', 'telefone', 'porta', 'azul', 'neve', 'avião', 'café', 'professor', 'navio', 'rio', 'água', 'escola', 'bola', 'prata', 'verde', 'rosa', 'suco', 'doces', 'cadeira'],

    ['escola', 'terra', 'livro', 'papel', 'diamante', 'mesa', 'íris', 'sol', 'chá', 'flor', 'rosa', 'salgados', 'suco', 'ceia', 'porta', 'árvore', 'fogo', 'branco', 'tempo', 'bicicleta', 'telefone', 'aluno', 'neve', 'bola', 'verde', 'azul', 'fruta', 'lápis', 'água', 'viagem'],

    ['diamante', 'rio', 'vermelho', 'terra', 'vento', 'branco', 'ouro', 'azul', 'cidade', 'neve', 'praia', 'fruta', 'verde', 'lua', 'cachorro', 'arco', 'bicicleta', 'caderno', 'ceia', 'papel', 'bola', 'suco', 'casa', 'navio', 'preto', 'tempo', 'fogo', 'camisa', 'árvore', 'íris'],

    ['tempo', 'marron', 'diamante', 'sapato', 'salgados', 'relógio', 'rio', 'jantar', 'escola', 'professor', 'suco', 'vermelho', 'rosa', 'amarelo', 'cachorro', 'vento', 'montanha', 'íris', 'helicóptero', 'avião', 'terra', 'branco', 'ferro', 'fruta', 'árvore', 'computador', 'estrada', 'verde', 'janela', 'livro'],

    ['íris', 'verde', 'montanha', 'jantar', 'branco', 'bola', 'aluno', 'camisa', 'lápis', 'casa', 'doces', 'amigo', 'suco', 'sapato', 'cachorro', 'chuva', 'árvore', 'avião', 'cidade', 'cadeira', 'viagem', 'mar', 'helicóptero', 'escola', 'caderno', 'diamante', 'relógio', 'sol', 'computador', 'professor'],

    ['bola', 'tempo', 'ferro', 'suco', 'verde', 'nuvem', 'jantar', 'amarelo', 'bicicleta', 'fogo', 'cachorro', 'cidade', 'vermelho', 'rosa', 'aluno', 'café', 'céu', 'árvore', 'estrada', 'moto', 'terra', 'camisa', 'janela', 'lua', 'praia', 'ceia', 'professor', 'vento', 'caderno', 'marron']

]
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(2)

pyautogui.write('w3scholls')
pyautogui.press("enter")
time.sleep(2)

cont = 0
i = 5
cont_vet = 5
for i in range (60):
    palavra = palavras[5][i]
    pyautogui.hotkey("ctrl","t")
    pyautogui.hotkey("ctrl","1")
    pyautogui.hotkey("ctrl","w")
    pyautogui.click(x=206, y=416)
    pyautogui.write(palavra)
    pyautogui.press('enter')
    time.sleep(5)
    cont += 1
    if (cont == 30):
        cont_vet += 1
        i = 0
        pyautogui.click(x=28, y=33)
        time.sleep(1)
        pyautogui.click(x=206, y=416)
        time.sleep(1)



pyautogui.hotkey("ctrl","w")
print("Pesquisa no Edge Concluida :)")