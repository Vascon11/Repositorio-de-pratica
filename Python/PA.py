#solicita ao usuario que digite o primeiro termo da PA
x=int(input("primeiro termo: "))

#solicita ao usuario que digite a razão da PA
y=int(input("ração da PA: "))

#solicita ao usuario que digite ate qual termo ele quer contar
z=int(input("até qual o termo que voce quer contar? ex(10): "))


while z>0:#while enquanto z for maior que 0, poderia sim ser uma for
    print("{} → ".format(x), end="")#imprime o termo atual d PA
    z-=1 #decrementa o contador de termos
    x+=y #adiciona a razao ao termo atual para o proximo termo


    #imprime o simbolo de infinito para indicar o fim
print("∞")