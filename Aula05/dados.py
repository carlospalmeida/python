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
        categoria2 = open(arquivo2, 'r',encoding='utf = 8')
        listaCategoria2 = {}
        contador2 = 0
        listaCategoria2["Tabela"] = "Categoria"
        listaCategoria2["Dados"] = ""
        dadosCategoria2 = {}
        for linhas2 in categoria2:
            colunas2 = linhas2.strip().split(';')
            contador2 += 1
            dadosCategoria2 [colunas2[0]] = {'nome': colunas2[1], 'Quantidades' : colunas2[2],'Embalagem':colunas2[3],'E1':colunas2[4],'E2':colunas2[5],'E3':colunas2[6],'E4':colunas2[7],'E5':colunas2[8],'E6':colunas2[9]}
        listaCategoria2["Dados"] = dadosCategoria2
        listaCategoria2["Total"] = contador2
        return(listaCategoria2)
        
        
        
        
        