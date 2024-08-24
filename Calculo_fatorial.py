#from math import factorial
#esse codigo pode ser execultado ultilizando a biblioteca math
#porém por eu querer escrever a equação, fiz o codigo para digitar um por um

#Solicita ao usuário que digite um número para calcular o fatorial
x=int(input("Digite um numero que possa ser fatorado: "))

#inicializa a variável z com 1, que será usada para calcular o fatorial
z=1

#start do while enquanto x for maior que 0
while x>0:
    y=x #atribui o valor de x a y
    print("{}".format(y), end="")# Imprime o valor de y
    print("x"if x>1 else "=", end="")
    z*=y  #multiplica z pelo valor de y
    x-=1  #decrementa o valor de x em 1

#imprime o resultado final do fatorial
print(z)