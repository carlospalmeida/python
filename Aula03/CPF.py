from validate_docbr import CPF
cpf = CPF()  # chamando a classe via variavel / instanciando a classe

print(cpf.validate("012.345.678-90"))
print(cpf.validate("012.345.678-91"))
print(cpf.validate("01234567890"))
