from dados import importacao
imp = importacao()

categoria = imp.impCategoria()
id = input('informe o codigo: ')
print(categoria["Dados"][id]["nome"])