def binario_para_decimal(binario):
    try:
        # Converte o número binário (string) em decimal
        decimal = int(binario, 2)
        return decimal
    except ValueError:
        # Caso o número binário seja inválido
        return "Entrada inválida! Por favor, insira apenas 0s e 1s."

# Solicita ao usuário para inserir um número binário
numero_binario = input("Insira um número binário: ")

# Converte e exibe o resultado
resultado = binario_para_decimal(numero_binario)
print(f"O número binário {numero_binario} em decimal é: {resultado}")