h = z = 0  # inicializa as variáveis h (soma dos números) e z (contador de números) com 0

# solicita ao usuário que insira um número para somar, informando que 999 encerra o programa
x = int(input("Digite um número para somar [digite 999 para parar]: "))

while x != 999:  # enquanto o número inserido for diferente de 999, o loop continua
    h += x  # adiciona o número inserido à soma total
    z += 1  # incrementa o contador de números digitados
    # solicita ao usuário que insira outro número para somar
    x = int(input("Digite um número para somar [digite 999 para parar]: "))

# após sair do loop, imprime a quantidade de números digitados e a soma total
print("Você digitou {} números com a soma resultando em {}".format(z, h))
