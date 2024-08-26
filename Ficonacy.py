# solicita ao usuário que insira a quantidade de termos da sequência que deseja mostrar
x = int(input("Quantos termos você quer mostrar? "))

# inicializa as variáveis i (primeiro termo da sequência) e h (segundo termo da sequência)
i = 0
h = 1

# imprime os dois primeiros termos da sequência
print("{}→{}→".format(i, h), end="")

# while loop para gerar e mostrar os termos subsequentes da sequência
while x > 0:
    r = i + h  # calcula o próximo termo da sequência como a soma dos dois anteriores
    print("{}→".format(r), end="")  # imprime o próximo termo da sequência
    i = h  # atualiza o valor de i para o próximo termo
    h = r  # atualiza o valor de h para o próximo termo
    x -= 1  # decrementa o contador de termos a serem mostrados

# imprime o símbolo de infinito para indicar o fim da sequência
print("∞")
