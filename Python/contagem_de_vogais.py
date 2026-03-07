palavras=("aprender","programar", "linguagem", "python",
          "curso", "gratis", "estudar" , "praticar",
          "trabalhar", "mercado", "programador", "futuro")
#liosta de palavras

for p in palavras:
    
    print(f"\nNa palavra {p.upper()} temos ", end="")
    
    #pega as palavras e passa letra por letra filtrando
    for letra in p:
        if letra.lower() in "aeiou":
            print(f" {letra}", end="")
