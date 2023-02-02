class importacao:
    def impCategoria(self):
        import os
        # cwd pega o caminho da pasta atual
        #caminho do arquivo
        arquivo = os.path.dirname(os.path.realpath(__file__)) + '\\BaseDados\\categorias.csv'
        #abrir arquivo
        # 'r' = read (leitura) / 'w' = write (escrever)
        # 'rw' ou 'wr' = (leitura e escrita)
        # encoding - tipo de arquivo (acentos e caracteres especiais) 
        categorias = open(arquivo, 'r', encoding='utf-8')
        #criar uma variavel para guardar os valores
        listaCategoria = {} #dicionario é muito parecido com o json
        contador = 0
        listaCategoria["Tabela"] = "Categoria"
        listaCategoria["Dados"] = ""
        dadosCategoria = {}
        for linhas in categorias:
            colunas = linhas.strip().split(';')
            contador += 1
            dadosCategoria[colunas[0]] = {'nome': colunas[1], 'Descrição' : colunas[2]}
            #print(dadosCategoria)
        listaCategoria["Total"] = contador
        listaCategoria["Dados"] = dadosCategoria
        return (listaCategoria)
        #print(contador)

    def impProdutos(self):
            import os
            arquivo2 = os.path.dirname(os.path.realpath(__file__)) + '\\BaseDados\\produtos.csv'
            produtos = open(arquivo2, 'r',encoding='utf = 8')
            listaProdutos = {}
            contador2 = 0
            listaProdutos["Tabela"] = "Categoria"
            listaProdutos["Dados"] = ""
            dadosProdutos = {}
            for linhas2 in produtos:
                colunas2 = linhas2.strip().split(';')
                contador2 += 1
                dadosProdutos [colunas2[0]] = {'nome': colunas2[1], 'categoria' : colunas2[2],'unidade':colunas2[3],
                'estoque':colunas2[4],'qtnpedida':colunas2[5],'nivelestoque':colunas2[6],'descontinuado':colunas2[7],
                'vlrvenda':colunas2[8],'vlrcusto':colunas2[9]}
            listaProdutos["Dados"] = dadosProdutos
            listaProdutos["Total"] = contador2
            return(listaProdutos)
            