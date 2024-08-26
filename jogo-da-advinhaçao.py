import random  # importa o módulo random para gerar números aleatórios

pal = 0  # inicializa o contador de palpites com 0

# gera um número aleatório entre 0 e 10 e o armazena na variável y
y = random.randint(0, 10)

# informa ao usuário que o programa pensou em um número entre 0 e 10
print("Acabei de pensar em um número entre 0 e 10!")

# solicita ao usuário que tente adivinhar o número
x = int(input("Você consegue adivinhar o número? "))

# while loop que continua até que o usuário acerte o número
while x != y:
    if x > y:  # se o palpite do usuário for maior que o número, informa que o número é menor
        x = int(input("O número que eu pensei é menor! "))
        pal += 1  # incrementa o contador de palpites
    else:  # se o palpite do usuário for menor que o número, informa que o número é maior
        x = int(input("O número que eu pensei é maior! "))
        pal += 1  # incrementa o contador de palpites
    
    # imprime uma linha de separação para formatar a saída
    print("-=-=-=" * 3, "-")
    
# quando o usuário acertar, imprime a mensagem de parabéns e o número de tentativas
print("Parabéns, você acertou! Depois de {} tentativas".format(pal))
