from random import randint
t=0
while True:
    print("-"*30)
    while True:
        n=input("Digite um numero: ")
        if n in "1234567890":
            n=int(n)
            break
    while True:
        p=str(input("Par ou Impar? [P/I]: ")).lower().strip()
        if p in "pi":
            break
    print("-"*30)
    m=randint(0,9)
    r=(n+m)%2
    if p =="i":
        if r==1:
            print(f"voce venceu! eu escolhi {m}")
            t+=1
        else:
            print(f"voce perdeu! eu escolhi {m}, {m} + {n} = {(m+n)}")  
            while True:
                h=str(input("quer continuar? [s/n]: ")).lower().strip()
                if h in "ns":
                    if h=="n":
                        acabou = True
                    break
    elif p=="p":
        if r==0:
            print(f"voce venceu, eu escolhi {m}")
            t+=1
        else:
            print(f"voce perdeu! eu escolhi {m}, {m} + {n} = {(m+n)}")
            while True:
                h=str(input("quer continuar? [s/n]: ")).lower().strip()
                if h in "ns":
                    if h=="n":
                        acabou = True
                    break
            if acabou == True:
                break 
print(f"voce vendeu {t} vezes")