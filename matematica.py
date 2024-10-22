import random
import time

operadores = ['+', '-', '*', '/']
números = range(1, 101)
tempo_resposta = 1
n_operações = 10

for i in range(n_operações):
  n1 = random.choice(números)
  n2 = random.choice(números)
  operador = random.choice(operadores)
  expressão = f'{n1} {operador} {n2}'
  resposta_correta = eval(expressão)

  print(f'Questão {i+1}: {expressão}')
  resposta_usuario = int(input('Sua resposta: '))

  if resposta_usuario == resposta_correta:
    print('Parabéns! Você acertou!')
  else:
    print(f'Resposta incorreta. A resposta correta era {resposta_correta}')

  time.sleep(tempo_resposta)