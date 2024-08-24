sex = str(input('Digite seu sexo: ')).upper().strip()
while sex not in "MmFf":
    sex = str(input("Digite o seu sexo [M/F]: ")).upper().strip()
print("Sua sexualidade foi registrada com secesso ,{}".format(sex))