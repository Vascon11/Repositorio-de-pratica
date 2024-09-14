#crie um programa que tenha uma tupla uncica com nomes de produtos
# e seus respectivos preços, na squencia. no final mostre uma 
# listagem de preços, organizando os dados em forma tabular.
lista =("lapis", 1.75,
        "borracha",2,
        "caderno",15.90,
        "estojo",25,
        "transferidor", 4.20,
        "compasso", 9.99,
        "mochila",120.32,
        "canetas",22.30,
        "livro",34.90)
#Lista de itens sendo o numero par
#e o valor do item sendo o numero inpar da tupla

print("-"*40)
print("LISTAGEM DE PREÇOS".center(40))
print("-"*40)
#titulo


for item in range(0,len(lista)):
    
    #se o item for par
    if item %2==0:
        print(f"{lista[item]:.<30}",end="")
        
    #se o item for impar fazer tal coisa
    else:
        print(f"R$ {lista[item]:>7.2f}")
        
print("-"*40)