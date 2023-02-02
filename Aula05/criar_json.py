from dados import importacao

imp = importacao()

categoria = imp.impCategoria()
produtos = imp.impProdutos()

id = input('informe o codigo do produto: ')

nome = produtos["Dados"][id]["nome"]
cat = produtos["Dados"][id]["categoria"]
nomeCategoria = categoria["Dados"][cat]["nome"]
precoVenda = produtos["Dados"][id]["vlrvenda"]
print(f'Produto: {nome}\nCategoria: {nomeCategoria}\nValor de venda: R$ {precoVenda}')
#print(produtos)



