# solicita ao usuário que digite seu sexo e converte a entrada para maiúsculas, removendo espaços extras
sex = str(input('Digite seu sexo: ')).upper().strip()

# while loop que continua enquanto a entrada não for 'M' ou 'F'
while sex not in "MF":
    # solicita novamente o sexo caso a entrada seja inválida
    sex = str(input("Digite o seu sexo [M/F]: ")).upper().strip()

# exibe uma mensagem de confirmação quando o sexo for registrado corretamente
print("Seu sexo foi registrado com sucesso: {}".format(sex))
