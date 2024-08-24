h=z=0
x=int(input("Digite um numero para somar [digite 999 para parar]: "))
while x!=999:
    h+=x
    z+=1
    x=int(input("Digite um numero para somar [digite 999 para parar]: "))
print("voce digitou {} numeros com a soma resuldando em {}".format(z,h))