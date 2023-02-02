from dados import importacao
imp = importacao()

categoria = imp.impCategoria()
id = input('informe o codigo: ')
print(categoria["Dados"][id]["nome"])
produtos = imp.impProdutos()

id = input('informe o cd de 1 a 77: ')
print(produtos["Dados"][id]["nome"])
