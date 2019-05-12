import random

resultado = []
while len(resultado) <= 15:
    numero = random.randint(15, 100)
    if numero not in resultado:
        resultado.append(numero)

resultado.sort()
print(resultado)