from random import randint
#importando o codigo da biblioteca

#tupla com numeros aleatorios
num=randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)

#mostra apenas o texto
print("os valores sorteados foram: ",end="")

for t in num:
    print(f"{t} ",end="")
    #mostra os numeros sorteados
    

print(f"\nE o maior valor da tupla foi {max(num)}")
#o comando max pega o maior valor da tupla

print(f"e o menor foi {min(num)}")
#o comando min pega o menor valor da tupla