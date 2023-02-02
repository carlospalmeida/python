'''
    web Scraping
    baixar as blibiotecas
    > pip install resquests
    > pip install beautifulsoup4

    
    ele vai ler a pagina e a tabela e criar um documento em html(xml ou json como vimos aula passada)
'''
from os import system, name
from requests import get # ler um endereço na internet
from bs4 import BeautifulSoup # interpretar uma pagina web

system('cls') if(name == 'nt') else system('clear')

url ='https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o'
response = get(url) # faz a leitura da pagina indicada
print(response) #imprimi a reposta da pagina
pagina = BeautifulSoup(response.text, 'html.parser') # imterpreta o HTML
tabela = pagina.find_all('table')
arquivo = open("tabela_paises.html",mode = "w", encoding="utf-8")
#arquivo.write(tabela[0].text)
print('Quantidade de tabelas:',len(tabela)) # Mostra quantas tabelas tem! use len para contar
linhas = tabela[0].find_all('tr') # separa as linhas da tabela[0]
print('Quantidade de linhas na tabela: ',len(linhas)) # Mostra quantas linhas na tabelas tem!

for i in range(1, len(linhas)):
    colunas = linhas[i].find_all('td')
    arquivo.write(str(i) + ' - ' + (colunas[1].text).strip() + '\n')