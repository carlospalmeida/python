import math

num1 = float(input('Insira um número:'))
num2 = float(input('Insira um número:'))
resultado = num1 / num2
print(resultado)
print(f'{resultado:.2f}')
print(round(resultado, 2))
# ceil = aredondamento para cima
print(math.ceil(resultado))
# pega a parte inteira do numereo
print(math.floor(resultado))
# mod = pega o resto de uma divisão
print(math.fmod(num1, num2))

##################




