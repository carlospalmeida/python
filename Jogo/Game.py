import random
from os import system, name

system('cls') if(name == 'nt') else system('clear')
system('color a')

valor = random.randrange(1, 100)

print("Tente adivinhar o numero de 1 a 100: ")
numero = 0

while (valor != numero):
    numero = int(input('informe um numero: '))
    if(numero == valor):
        print('Parabens você acertou!!')
    elif(numero > valor):
        print('o numero era menor!')
    elif(numero < valor):
        print('o numero era maior')
print(f'o valor era {valor}')
input()
system('color')
system('cls')


