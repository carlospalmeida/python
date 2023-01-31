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
