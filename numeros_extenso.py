#foi feito uma tupla com strings de 0 á 20 escritas
numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", 
    "seis", "sete", "oito", "nove", "dez", "onze", 
    "doze", "treze", "quatorze", "quinze", "dezesseis", 
    "dezessete", "dezoito", "dezenove", "vinte"
)
continuar = "S" #aprenas definil algo para a var "continuar"

while continuar != "N":
    #while para caso o numero digitado nao ser o solicidado

    while True:
        num = int(input("Digite um número entre 0 e 20: "))
        
        #caso o numero escrito esteja entre 0 e 20 ele ira quebrar a while, ou ira solicidar um novo numero
        if 0<=num<=20:
            break
        else:
            print("tente novamente")
    #irá printar o numero por estenso solicidado
    print(numeros_por_extenso[num])

    #Filtra a letra que foi digitada para que a varavel "continuar"
    #so aceitasse "S" ou "N"
    while True:
        continuar = input("Quer continuar?[S/N] ").upper().strip()
        if continuar in ["S","N"]:
            break