import random
pal=0

y = random.randint(0, 10)
print("Acabei de pensar em um numero entre 0 e 10!")
x=int(input("Voce consegue adivinhar o numero? "))
while x !=y:
    if x>y:
        x=int(input("O numero que eu pensei é menor!"))
        pal+=1
    else:
        x=int(input("O numero que eu pensei é maior: "))
        pal+=1
    print("-=-=-="*3,"-")
print("Parabéns, voce acertou! depois de {} tentativas".format(pal))