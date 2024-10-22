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
pyautogui.FAILSAFE
pyautogui.PAUSE = 0.3

palavras = [

    ['suco', 'cha', 'computador', 'viagem', 'arvore', 'amarelo', 'cidade', 'salgados', 'marron', 'montanha', 'navio', 'papel', 'chuva', 'fogo', 'caderno', 'porta', 'amigo', 'ceia', 'aviao', 'bicicleta', 'gato', 'helicoptero', 'aluno', 'casa', 'fruta', 'nuvem', 'azul', 'rosa', 'vermelho', 'sapato'],

    ['praia', 'sol', 'rio', 'mesa', 'cadeira', 'janela', 'vidro', 'barco', 'caminho', 'estrada', 'ponte', 'predio', 'farmacia', 'mercado', 'padaria', 'salada', 'relogio', 'tigre', 'urso', 'girafa', 'leao', 'cobra', 'lagarto', 'pato', 'galinha', 'porco', 'vaca', 'ovelha', 'cavalo', 'escola', 'universidade'],

    ['carro', 'moto', 'onibus', 'trem', 'aviao', 'helicoptero', 'navio', 'bicicleta', 'patins', 'skate', 'caminhao', 'metrô', 'trator', 'barco', 'jangada', 'submarino', 'nave', 'foguete', 'parque', 'praia', 'floresta', 'deserto', 'lago', 'oceano', 'mar', 'planalto', 'serra', 'colina', 'cachoeira', 'ilha', 'glaciar'],

    ['pincel', 'tinta', 'caneta', 'lapis', 'caderno', 'borracha', 'estojo', 'regua', 'pasta', 'grampeador', 'tesoura', 'papel', 'bloco', 'cartolina', 'cola', 'clipes', 'durex', 'calculadora', 'livro', 'revista', 'jornal', 'quadro', 'pincel', 'giz', 'apagador', 'mesa', 'cadeira', 'projetor', 'tela', 'monitor'],

    ['luz', 'lampada', 'ventilador', 'ar', 'ventilador', 'geladeira', 'fogao', 'microondas', 'liquidificador', 'batedeira', 'ferro', 'cafeteira', 'torradeira', 'espremedor', 'chaleira', 'forno', 'aspirador', 'televisao', 'radio', 'som', 'computador', 'notebook', 'tablet', 'celular', 'bateria', 'carregador', 'teclado', 'mouse', 'monitor', 'cabos'],

    ['agua', 'suco', 'refrigerante', 'cerveja', 'vinho', 'cafe', 'cha', 'leite', 'achocolatado', 'suco', 'vitamina', 'agua', 'soda', 'guarana', 'laranja', 'morango', 'limao', 'uva', 'abacaxi', 'coco', 'manga', 'melancia', 'kiwi', 'banana', 'goiaba', 'abacate', 'tomate', 'pepino', 'cenoura', 'batata', 'beterraba'],

    ['abobora', 'chuchu', 'abobrinha', 'pimentao', 'berinjela', 'alho', 'cebola', 'salsinha', 'coentro', 'manjericao', 'hortela', 'alecrim', 'oregano', 'tomilho', 'couve', 'espinafre', 'alface', 'rucula', 'agrião', 'repolho', 'brocolis', 'couveflor', 'ervilha', 'milho', 'soja', 'feijao', 'lentilha', 'grao', 'arroz', 'trigo'],

    ['pao', 'bolo', 'torta', 'biscoito', 'bolacha', 'pipoca', 'salgadinho', 'pastel', 'coxinha', 'empada', 'quiche', 'pizza', 'esfiha', 'kibe', 'quibe', 'tapioca', 'crepioca', 'paozinho', 'baguete', 'croissant', 'torta', 'empada', 'pao', 'pizzaiolo', 'cozinheiro', 'garcom', 'chef', 'restaurante', 'lanchonete', 'bar'],

    ['pintura', 'escultura', 'arquitetura', 'design', 'fotografia', 'cinema', 'teatro', 'musica', 'danca', 'literatura', 'poesia', 'prosa', 'contos', 'romance', 'novela', 'tragedia', 'comedia', 'suspense', 'drama', 'policial', 'cientifico', 'fantasia', 'ficcao', 'realismo', 'modernismo', 'barroco', 'renascimento', 'cubismo', 'surrealismo', 'impressionismo'],

    ['arte', 'museu', 'galeria', 'exposicao', 'feira', 'teatro', 'salao', 'auditorio', 'palco', 'plateia', 'atencao', 'foco', 'inteligencia', 'criatividade', 'habilidade', 'diligencia', 'disciplina', 'dedicacao', 'esforco', 'perseveranca', 'coragem', 'honra', 'lealdade', 'amizade', 'companheirismo', 'generosidade', 'bondade', 'sinceridade', 'honestidade', 'respeito']

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
cont_vet = 3
outr_cont = 0
for i in range (60):
    palavra = palavras[cont_vet][outr_cont]
    pyautogui.hotkey("ctrl","t")
    pyautogui.hotkey("ctrl","1")
    pyautogui.hotkey("ctrl","w")
    pyautogui.click(x=206, y=416)
    pyautogui.write(palavra)
    pyautogui.press('enter')
    time.sleep(5)
    outr_cont += 1
    cont += 1
    if (cont == 30):
        cont_vet += 1
        outr_cont = 0
        pyautogui.click(x=28, y=33)
        time.sleep(1)
        pyautogui.click(x=206, y=416)
        time.sleep(1)



pyautogui.hotkey("ctrl","w")
print("Pesquisa no Edge Concluida :)")
print("Iniciando 'Idle Slayer' em:")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("'Idle Slayer' em execução :)")

#_________________________________________________________________________________________
#                                Pesquisa no Edge encerrada
#_________________________________________________________________________________________

#_________________________________________________________________________________________
#                                   Começando Idle Slayer
#_________________________________________________________________________________________

#abrir Idle Slayer + Steam
pyautogui.press("win")
pyautogui.write("idle")
pyautogui.press("enter")
time.sleep(15)

#Desativando Janela de permição Segurança Steam


#Escolhendo o Usuário
pyautogui.click(x=811, y=583)
time.sleep(14)

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