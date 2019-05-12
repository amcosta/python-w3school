import random


def embaralhar(texto):
    lista = list(texto)
    random.shuffle(lista)
    return lista


texto = input('Digite um texto: ')
print(''.join(embaralhar(texto)))
