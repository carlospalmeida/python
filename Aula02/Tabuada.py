# Importar biblioteca
from os import system, name
# "==" é para comparação!
# > maior / < menor / >= maior igual
# != diferente / <= menor igual
if (name == 'nt'):
    system('cls')
else:
    system('clear')

print('!TABUADA!')
multiplicador = int(input('Escolha um número de 1 a 10:'))
#criar loop - repetição de codigo
#for = comando usado para criar loop
# i = variavel (pode ser qualquer nome)
# range = usado para indicar quantas vezez sera feito o loop 
for i in range(11):
    resultado = i * multiplicador
    #print(' {} * {} = {}' . format(multiplicador, i, resultado))
    print(f' {multiplicador} * {i:>2} = {resultado:>3}')





