while True:  #while loop infinito que continua até encontrar um break
    # solicita ao usuário que insira o número da tabuada que ele deseja
    x = int(input("Qual tabuada quer saber? [número negativo cancela] ")) 
    
    if x < 0:  #verifica se o número é negativo
        break  #se for negativo, encerra o loop e termina o programa
    
    #imprime uma linha de separação para formatar a saída
    print("-" * 15)  
    
    #for loop para calcular e imprimir a tabuada do número inserido
    for y in range(1, 11):  
        # imprime o resultado da multiplicação na forma 'x X y = resultado'
        print(f"{x} X {y} = {x*y}")  
    
    #imprime outra linha de separação para finalizar a tabuada
    print("-" * 15)
