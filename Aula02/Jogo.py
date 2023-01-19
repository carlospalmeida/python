import random

valor = random.randrange(1, 100)
print('tente adivinhar o número de 1 a 100')
numero = 0
while (valor != numero):
    numero = int(input('Informe o número: '))
    if(numero == valor):
        print('Você acertou')
    elif (numero > valor):
        print('O numero era menor')
    elif (numero < valor):
        print('o Numero era maior')
print(f'o número era: {valor}')

