while True:
    x=int(input("Qual taboada quer saber?[numero negativo cancela] "))
    if x <0:
        break
    print("-"*15)
    for y in range(1,11):
        print(f"{x} X {y} = {x*y}")
    print("-"*15)