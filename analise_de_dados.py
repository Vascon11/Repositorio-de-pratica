num1= int(input("Digite um numero: "))
num2= int(input("Digite um numero: "))
num3= int(input("Digite um numero: "))
num4= int(input("Digite um numero: "))
n=num1,num2,num3,num4

print(n)

#quantas vezes apareceu o valor 9
if 9 in n:
    print(f"o numero 9 apareceu {n.count(9)} vezes")
    
#em que posição foi digitado o primeiro valor 3
if 3 in n:
    print(f"O numero primeiro 3 foi digitado na posição {n.index(3)+1} ")

for a in n:
    if a%2 ==0:
        print(f"esse numero é par {a}")
#quais foram os numeros pares