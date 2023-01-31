"""
Calculadora

"""
from os import system, name
import math
from pickle import TRUE
sair = 's'

while (sair.upper() =='S'):

    system('cls') if(name == 'nt') else system('clear')

    print('CALCULADORA'.center(80,'*'))
    print('''
    Escolha uma das opções:
    [1] - soma
    [2] - subtração
    [3] - Multiplicação
    [4] - Divisão
    ''')
    opcao = input('Digite sua escolha: ')
    continuar = True
    while (continuar):
        if(opcao.isdecimal()):
            opcao = int(opcao)
            if(opcao >= 0 and opcao <= 4):
                continuar = False
            else:
                opcao = input('Digite um valor de 1 a 4(apenas) ou aperte x para sair: ')
                if(opcao.upper()== 'X'):
                    system('cls') if(name == 'nt') else system('clear')
                    exit()
        

    
    
    
    opcao = int(opcao)
    if (opcao == 1):
        
        n1 = input('Digite um número: ')
        n2 = input('Digite um número: ')
        n1 = float(n1)
        n2 = float(n2)
        soma = n1 + n2
        print(f'Resultado: {soma}')
    if (opcao == 2): 
        n1 = input('Digite um número: ')
        n2 = input('Digite um número: ')
        n1 = float(n1)
        n2 = float(n2)
        subt = n1 - n2
        print(f'Resultado: {subt}')
    if (opcao == 3):
        n1 = input('Digite um número: ')
        n2 = input('Digite um número: ')
        n1 = float(n1)
        n2 = float(n2)
        multi = n1 * n2
        print(f'Resultado: {multi}')
    if (opcao == 4):
        n1 = input('Digite um número: ')
        n2 = input('Digite um número: ')
        n1 = float(n1)
        n2 = float(n2)
        Div = n1 / n2
        print(f'Resultado: {Div}')

    
    sair = input('''
    Deseja continuar?,digite [s] para sim ou [x] para sair: 
    ''')
    system('cls') if(name == 'nt') else system('clear')
