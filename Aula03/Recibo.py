from num2words import num2words
from os import system, name

def validarNumero(numero):
    numero = numero.replace(',','.')
    try:
        resultado = float(numero)
    except:
        resultado = 0
    return resultado


system('cls') if(name == 'nt') else system('clear')
print('RECIBO'.center(80,"*"))
print('')
nome = input('Informe o nome: ')
valor = input('Informe o valor:')
valor = validarNumero(valor)
extenso = (num2words(valor, to='currency', lang='pt_BR'))
valor =float(valor) 
numeroBR = f'{valor:_.2f}'.replace('.',',').replace('_','.')
recibo = f'Recebemos de {nome}\nO valor de {extenso} (R$ {numeroBR})'
print(recibo)
#print(valor.isdecimal())
#if (valor.isdecimal()):
#    print('ok')

 



