from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from os import system, name
from getpass import getpass

system('cls') if(name == "nt") else system('clear')

#Função Clicar
def clicar(xpath):
    try:
        clique = chrome.find_element(By.XPATH , xpath)
        clique.click()
        sleep(2)
    except:
        print(f"ERROR NO XPATH: {xpath}")


#Função Escrever
def escrever(xpath, texto):
    try:
        digitar = chrome.find_element(By.XPATH ,xpath)
        digitar.send_keys(texto)
        sleep(2)
    except:
        print(f'ERRO NO XPATH:'[xpath])



LoginSenac = input("Insira seu login: ")
SenhaSenac = getpass("Insira sua senha: ")

site = 'https://www.sp.senac.br'

chrome = webdriver.Chrome()
chrome.get(site)

#Aceitar cookies
botaoCookie = '//*[@id="mm-0"]/div[4]/div'
clicar(botaoCookie)

#Entrar no login
botaoBurger = '//*[@id="menu-mobile-ssp"]'
clicar(botaoBurger)
botaologin = '//*[@id="txtLoginNaoLogadoMob"]'
clicar(botaologin)

#Login
Login = '//*[@id="login-email"]'
clicar(Login)
escrever(Login,LoginSenac)

#Senha
senha = '//*[@id="login-password"]'
clicar(senha)
escrever(senha,SenhaSenac)

#Botão Logar
Entrar = '//*[@id="btnLoginHeader"]'
clicar(Entrar)


sleep(10)
system('cls')
print("EXECUÇÃO TERMINADA")

