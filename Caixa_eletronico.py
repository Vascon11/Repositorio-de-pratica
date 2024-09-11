#Imprime o Titulo do banco
print("="*34)
print(f"BANCO DO BRASIL".center(34))
print("="*34)

#pergunta o quanto quer sacar
saque=int(input("Digite o valora a ser sacado R$"))

# acresenta um valor para as variaveis, para contar as notas de 50, 20, 10 e 1 reais
cinquenta=vinte=dez=um=0

#inicia a while para saber a quantidade de cada nota
while saque!=0:
    if saque >=50:
        cinquenta+=1
        saque -=50
    elif saque >=20:
        vinte+=1
        saque -=20
    elif saque >=10:
        dez+=1
        saque -=10
    elif saque <= 10:
        um+=1
        saque -=1

#Aqui é para a quantidade de notas necessarias impresas, se caso precisar de 0 notas, ele não ira printar
print("portando será tirado as sequintes notas")
if cinquenta != 0:
    print(f"{cinquenta} notas de 50R$")
if vinte != 0:
    print(f"{vinte} notas de 20R$")
if dez != 0:
    print(f"{dez} notas de 10R$")
if um != 0:
    print(f"{um} notas de 1R$")