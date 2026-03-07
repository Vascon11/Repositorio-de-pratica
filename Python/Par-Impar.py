from random import randint  #importa a funcao randint do modulo random para gerar numeros aleatorios

t = acabou = 0  #inicializa o contador de vitorias do jogador

while True:  #loop principal que continua ate o jogador decidir parar
    print("-" * 30)  #imprime uma linha de separacao para formatar a saida

    #loop para garantir que o usuario insira um numero valido
    while True:
        n = input("Digite um numero: ")[0]  #solicita ao usuario que insira um numero
        if n in "1234567890":  #verifica se a entrada e um numero valido (0 a 9)
            n = int(n)  #converte a entrada para um inteiro
            break  #sai do loop interno se a entrada for valida

    #loop para garantir que o usuario escolha entre "Par" ou "Impar"
    while True:
        p = str(input("Par ou Impar? [P/I]: ")).lower().strip()[0]  #solicita ao usuario que escolha "Par" ou "Impar"
        if p in "pi":  #verifica se a entrada e valida ('p' ou 'i')
            break  #sai do loop interno se a entrada for valida

    print("-" * 30)  #imprime uma linha de separacao para formatar a saida

    m = randint(0, 9)  #gera um numero aleatorio entre 0 e 9 para o computador
    r = (n + m) % 2  #calcula o resto da divisao da soma por 2 (0 = Par, 1 = Impar)

    #se o jogador escolheu "Impar"
    if p == "i":
        if r == 1:  #se o resultado for 1 (Impar)
            print(f"Voce venceu! Eu escolhi {m}")  #informa que o jogador venceu
            t += 1  #incrementa o contador de vitorias
        else:  #se o resultado for 0 (Par)
            print(f"Voce perdeu! Eu escolhi {m}, {m} + {n} = {(m+n)}")  #informa que o jogador perdeu
            #loop para perguntar se o jogador quer continuar
            while True:
                h = str(input("Quer continuar? [s/n]: ")).lower().strip()[0]  #pergunta se o jogador quer continuar
                if h in "ns":  #verifica se a entrada e valida ('s' ou 'n')
                    if h == "n":  #se a resposta for "n", o jogo acaba
                        acabou = True
                    break  #sai do loop se a entrada for valida

    #se o jogador escolheu "Par"
    elif p == "p":
        if r == 0:  #se o resultado for 0 (Par)
            print(f"Voce venceu, eu escolhi {m}")  #informa que o jogador venceu
            t += 1  #incrementa o contador de vitorias
        else:  #se o resultado for 1 (Impar)
            print(f"Voce perdeu! Eu escolhi {m}, {m} + {n} = {(m+n)}")  #informa que o jogador perdeu
            #loop para perguntar se o jogador quer continuar
            while True:
                h = str(input("Quer continuar? [s/n]: ")).lower().strip()  #pergunta se o jogador quer continuar
                if h in "ns":  #verifica se a entrada e valida ('s' ou 'n')
                    if h == "n":  #se a resposta for "n", o jogo acaba
                        acabou = 1
                    break  #sai do loop se a entrada for valida
            if acabou == 1:  #se o jogador decidiu parar, o jogo acaba
                break

print(f"Voce venceu {t} vezes")  #exibe o numero total de vitorias do jogador
