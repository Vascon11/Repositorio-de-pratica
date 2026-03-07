#tupals de times
times = (
    "Flamengo", "Palmeiras", 
    "São Paulo", "Corinthians", 
    "Santos","Grêmio", "Internacional", 
    "Atlético Mineiro","Fluminense",
    "Botafogo", "Vasco da Gama",
    "Cruzeiro","Athletico Paranaense", 
    "Bahia", "Ceará","Fortaleza",
    "Sport Recife", "Goiás", "Chapecoense",
    "Avaí"
)

#os 5 primeiros times

print("-"*148)#enfeites
print(f"Lista dos 5 primeiros times {times[0:5]}")

#os 4 ultimos

print("-"*148)#enfeites
print(f'Os 4 ultimos times são {times[-4:]}')

#times em ordem alfabetic

print("-"*148)#enfeites
print(f'Os times em ordem alfabetica {sorted(times[-4:])}')


#em que posição está o time da Chapecoense

print("-"*148)#enfeites
print(f"O chapecoense está na {times.index('Chapecoense')+1} posição")
print("-"*148)#enfeites