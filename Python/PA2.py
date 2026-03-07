#imprime o cabeçalho do gerador de PA
print("=-="*3,"Gerador de PA","=-="*3)

#solicita ao usuario que digite o primeiro termo da PA
x=int(input("primeiro termo: "))

#solicita ao usuario que digite a razão da PA
y=int(input("razão da PA: "))

#solicita ao usuario que digite ate qual termo ele quer contar
z=int(input("até qual o termo que voce quer contar? ex(10): "))

c=0#Vvalor de termos realizados

cont = True#uma var de controle para continuar ou parar o loop

#while principal que continua enquanto 'cont' for True
while cont == True:


    while z>0:#while enquanto z for maior que 0, poderia sim ser uma for

        print("{} → ".format(x), end="")#imprime o termo atual d PA
        z-=1 #decrementa o contador de termos
        x+=y #adiciona a razao ao termo atual para o proximo termo
        c+=1 #acresenta um termo

    print("PAUSE")#imprime o simbolo de infinito para indicar o fim

     #pergunta ao usuario se ele quer continuar
    seg=input("quer continuar?[S/N] ").lower() 


    if seg == "s":
        #se o usuário quiser continuar, solicita mais termos
        z=int(input("mais quantos termos? "))
        
    else: 
        #interrompe a while principal
        break

# Imprime a mensagem final com o numero total de termos gerados
print("Finalizado com {} termos".format(c))