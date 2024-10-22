import random as escolhe_ai
import time as tempinho
import pyautogui as progama # type: ignore

progama.PAUSE = 0.3


print("Siguinte, esse código é para escolher alguma coisa aleatória a forma e oque vai ser você escolhe.")

paciencia = 10
ativador = 1

tempinho.sleep(1)
while ativador == 1:
    # Início ou Reinício de programa {---------------------------------------------------------------------------------------------------
    if paciencia == 10:
        print("| Manda o Primeiro parâmetro aí pra nois, tens as seguintes opções |")
        parametro_inicial = int(input("Palavras - Digite 1, Numeros - Digite 2: "))
    else:    
        print("Te relembrando que as opções são:")
        parametro_inicial = int(input("Digitar o número 1 para palavra ou Digitar o número 2 para números: "))
    #------------------------------------------------------------------------------------------------------------------------------------}
    
    # Filtragem do requisito {-----------------------------------------------------------------------------------------------------------
    if parametro_inicial == 1:
        tempinho.sleep(1)
        print("Beleza ")
    elif parametro_inicial == 2:
        tempinho.sleep(1)
        print("Beleza!! vamos então para o próximo parâmetro que preciso")
        print("Você quer que seja escolhido um ou mais números dentre um intervalo imposto por você;")
        print("Ou")
        print("Que seja escolhido um ou mais números dentre os que você forneça")
        print("1 - Um número entre intervalo.")
        print("2 - Mais de um número entre os intervalos.")
        print("3 - Um número dentre os que forem digitados")
        print("4 - Mais de um número dentre os que forem digitados")
        parametro_secundario = int(input("Digite sua escolha: "))
        if parametro_secundario == 2 or parametro_secundario == 4:
            
            print("Os números sorteados podem ser repetidos?")
            repete = int(input("| 1 - Sim | 2 - Não | "))
            if repete == 2:
                print("Digite o intervalo dos números separados por vírgula;")
                intervalo = input("Exemplo: '1,6' do um ao seis | Seu intervalo: ") 
                primeiro, ultimo = intervalo.split(",")  
                primeiro = int(primeiro)  
                ultimo = int(ultimo)  
                quantidade = ultimo - primeiro
                vetor = []
                num = 1
                while primeiro <= ultimo:
                    vetor.append(primeiro)
                    primeiro += 1
                while vetor != []:
                    numero_sorteado = escolhe_ai.choice(vetor)
                    print(num, " - número:", numero_sorteado)  
                    num += 1
                    vetor.remove(numero_sorteado)
            elif repete == 1:
                print("Digite o intervalo dos números separados por vírgula;")
                intervalo = input("Exemplo: '1,6' do um ao seis | Seu intervalo: ") 
                primeiro, ultimo = intervalo.split(",")  
                primeiro = int(primeiro)  
                ultimo = int(ultimo)  
                quantidade = ultimo - primeiro
                vetor = []
                num = 1
                while primeiro <= ultimo:
                    vetor.append(primeiro)
                    primeiro += 1
                for i in range (len(vetor)) :
                    numero_sorteado = escolhe_ai.choice(vetor)
                    print(num, " - número:", numero_sorteado)  
                    num += 1
                    

        
    # paciência...
    else:
        if paciencia == 10: 
            print(".")
            tempinho.sleep(0.5)
            print(".")
            tempinho.sleep(0.5)
            print(" ")
            print(" ")
            print("Opa! Você digitou " , parametro_inicial , " que não se encaixa em nenhuma das opções que eu te dei.")
            print("Mas tudo bem, não se preucupe, é só tentar de novo :D")
        elif paciencia == 9: 
            print(".")
            tempinho.sleep(0.5)
            print(".")
            tempinho.sleep(0.5)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("Eita! você digitou errado novamente, mas vai lá tenta de novo")
        elif paciencia == 8:
            print(".")
            tempinho.sleep(0.5)
            print(".")
            tempinho.sleep(0.5)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("Nossa, pela terceira vez você digitou errado, (pela terceira vez...) Leia direitinho e tenta novamente")
            print("Você precisa responder algumas coisas para conseguirmos atingir seu pedido, esolha uma das duas opções.")        
        elif paciencia == 7: 
            print(".")
            tempinho.sleep(0.5)
            print(".")
            tempinho.sleep(0.5)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("Tá, tenta entender que você só precisa digitar um número entre um ou dois que definirá oque o progama deve fazer")
        elif paciencia == 6:
            print(".")
            tempinho.sleep(0.5)
            print(".")
            tempinho.sleep(0.5)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("Você consegue entender que a proposta do progama;")
            print("é te ajudar a com a problemática de escolher entre palavras ou números aleatórios??")
        elif paciencia == 5: 
            print(".")
            tempinho.sleep(0.5)
            print(".")
            tempinho.sleep(0.5)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("É...")
        elif paciencia == 4: 
            print(".")
            tempinho.sleep(0.5)
            print(".")
            tempinho.sleep(0.5)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("Poxa vida...")
        elif paciencia == 3: 
            tempinho.sleep(1.5)
        elif paciencia == 2: 
            progama.press("win")
            progama.write("Voce so precisa escolher entre 1 ou 2...")
            tempinho.sleep(2)
            progama.hotkey("ctrl", "a")
            progama.press("backspace")

            progama.write("E tao simples")
            tempinho.sleep(2)
            progama.hotkey("alt", "tab")
        elif paciencia == 1:
            print(" ")
            print(" >:( ")
            print(" ")
        else:
            print("Eu desisto, nunca mais me procure")
            tempinho.sleep(4)
            progama.hotkey("alt","f4")        
        paciencia -= 1
    #------------------------------------------------------------------------------------------------------------------------------------}



de, a = input("Digite ")
