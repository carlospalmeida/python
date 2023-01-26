"""
Jogo: Papel,pedra e Tesoura

    objetivo:
    Criar um jogo interativo onde iremos usar array(tupla)

    blibliotecas:
    Ramdom
    os

    Funções:
    iniciarJogo()
"""


from os import system, name
import random
sair = 'S'

while (sair.upper() == 'S'):
    system('cls') if(name == 'nt') else system('clear')
    print('''-------------------------
JOGO PEDRA,PAPEL E TESOUA
-------------------------

Escolha uma das opções para iniciar
 [0] Pedra
 [1] Papel
 [2] Tesoura
    ''')
    padrao = '\033[0;0m'

    opcao = input('Digite sua escolha: ')
    continuar = True
    while (continuar):
        if (opcao.isdecimal()):
            opcao = int(opcao)
            if(opcao >= 0 and opcao <= 2):
                continuar = False
            else:
                opcao = input('Coloque apenas numero de 0 a 2! ou aperte x para sair: ')
                if (opcao.upper() == 'X'):                    
                    system('cls') if(name == 'nt') else system('clear')
                    exit()
        else:
            opcao = input('Coloque apenas numero de 0 a 2! ou aperte x para sair: ')
            if (opcao.upper() == 'X'):
                system('cls') if(name == 'nt') else system('clear')
                exit()
                
    
    computador = random.randint(0,2)

    jogadas = (("Empate","Computador ganhou","Você ganhou"),
                ("Você ganhou","Empate","Computador ganhou"),
                ("Computador ganohu","você ganhou","Empate"))
    pecas = ('Pedra','Papel','Tesoura')
    
    #cores do terminal 
    fundo_branco = "\033[47m"
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;36m"
    REVERSE = "\033[;7m"
    letra_padrao = "\033[;7m"
    

    print(fundo_branco + BLUE + (f'{pecas[computador]} x {pecas[opcao]}').center(80))
    print(fundo_branco + RED + jogadas[computador][opcao].center(80))
    print(padrao)

    
    sair =input('''
Deseja continuar?
Aperte [S] para jogar novamente ou qualquer tacla para sair.
    ''')
    print(padrao)
    system('cls') if(name == 'nt') else system('clear')
    
