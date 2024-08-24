from time import sleep
#biblioteca que importa um modulo de tempo, onde voce consegue criar um "deley" ulitlizado na linha 47

#Inicializa as variáveis h e z com o valor 0, que serão usadas posteriormente no loop e nas condições
h=z=0

# Entrada dos números pelo usuário
x=int(input("Primeiro numero: "))
y=int(input("Segundo numero: "))


#inicio da While onde será impreso o "menu"
while z == 0:
    # Exibe o menu de opções para o usuário escolher a operação desejada
    print("oque voce deseja realizar com esses numeros?")
    h=int(input("""
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] qual é o n° maior
[ 4 ] novos números
[ 5 ] sair do programa
>>>"""))
#aqui execultara os comandos pedido pelo usuario
    if h==5: #altera o valor da variavel Z, que encerra a while
        z=1

    elif h==4: #acresenta um novo valor para o "x" e "y"
        x=int(input("Primeiro numero: "))
        y=int(input("Segundo numero: "))

    elif h==3:
        if x>y: #faz uma filtragem para saber qual é o maior valor, e printa no terminal
            print("o numero maior é ",x)
        else:
            print("o numero maior é ",y)


    elif h==2: #Realiza a multiplização solicitada pelo usuario
        print(" {} x {} = {}".format(x,y,(x*y)))

    elif h==1: #Realiza a soma solicitada pelo usuario
        print(" {} + {} = {}".format(x,y,(x+y)))

    else: #Aparece essa mensagem quando o valor colocado pelo usuario nao seja reconhecivel pelo programa
          # todos os valores que nao sejam 1 2 3 4 5
        print("ERRO, tente novamente")

# Mensagem final após a escolha de sair do programa
print("Finalizando...")
sleep(3) #modulo de deley
print("Encerrado com sucesso!")
#fim do codigo