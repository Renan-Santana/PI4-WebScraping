# Realizar as instalações das libs abaixo
# pip install requests
# pip install pandas
# pip install beautifulsoup4
# pip install selenium

from faulthandler import is_enabled
from itertools import count
from lib2to3.pgen2.pgen import DFAState
from multiprocessing.util import is_exiting
import time
from tokenize import Double
from urllib import request
import requests
import pandas as pd
import heapq
import numpy as np
import re
import json
import csv
import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from sklearn.feature_extraction.text import TfidfTransformer
import nltk

#funcao para verificar se elemento existe na DOM


def is_element_present(how, what):
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException as e:
        return False
    return True


# leitura dos dados do json
with open("credenciais-exemplo.json", encoding='utf-8') as jsonCredenciais:
    credenciais = json.load(jsonCredenciais)

# url da página de login do twitter
urlTwitter = "https://twitter.com/i/flow/login"

# instacia do firefox
options = Options()
options.headless = True  # exibe o navegador
# executavel do geckdriver
service = Service(executable_path="geckodriver-v0.31.0-win64\geckodriver.exe")
driver = webdriver.Firefox(service=service)

# names = []
tweets = []


# abre pagina
driver.get(urlTwitter)


def login():
    # atribuicao de valores primeira tela
    xPathEmail = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"
    xPathAvancar = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div"

    # atribuicao de valores segunda tela
    xPathValidaNomeCelular = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input"
    xPathAvancarUsuario = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div"

    # atribuicao de valores terceira tela
    xPathSenha = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
    xPathEntrar = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div"

    time.sleep(3)

    # inicia login
    try:

        driver.find_element(By.XPATH, xPathEmail).send_keys(
            credenciais['email'])
        time.sleep(2)

        driver.find_element(By.XPATH, xPathAvancar).click()
        time.sleep(2)

        # verifica se elemento de verificação de usuario existe
        if is_element_present('xpath', xPathValidaNomeCelular):
            driver.find_element(By.XPATH, xPathValidaNomeCelular).send_keys(
                credenciais['nome'])
            time.sleep(2)

            driver.find_element(By.XPATH, xPathAvancarUsuario).click()
            time.sleep(2)

        driver.find_element(By.XPATH, xPathSenha).send_keys(
            credenciais['senha'])
        time.sleep(2)

        driver.find_element(By.XPATH, xPathEntrar).click()
        time.sleep(2)
    except Exception as e:
        driver.quit()
        print(e)
        return False
    return True


def search(name):
    # atribuicao de valores
    xPathSearchTwitter = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input"
    XPathLasted = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div/span"

    try:
        driver.find_element(By.XPATH, xPathSearchTwitter).send_keys(name)
        time.sleep(2)

        driver.find_element(By.XPATH, xPathSearchTwitter).send_keys(Keys.ENTER)
        time.sleep(2)

        driver.find_element(By.XPATH, XPathLasted).click()
        time.sleep(2)
    except Exception as e:
        driver.quit()
        print(e)

def limpeza_dados(dataset):
	# Para dividir um texto em frases *caso precise*: dataset = nltk.sent_tokenize(texto)
	for contador in range(len(dataset)):
            # Converte todas as palavras para para minúsculo.
            dataset[contador] = dataset[contador].lower()

            # Converte tudo que não seja uma palavra (exemplo: pontuação) para um espaço simples.
            dataset[contador] = re.sub(r'W', ' ', dataset[contador])

            # Converte todas as quebras de linha para um espaço simples.
            dataset[contador] = re.sub(r's+', ' ', dataset[contador])

def repeticao_palavras(dataset):
	contador_palavras = {}
	for dados in range(len(dataset)):
            # print(dataset.loc[dados,"Tweets"])
            palavras_tokenizadas = nltk.word_tokenize(dados)
            for palavra in palavras_tokenizadas:
                if palavra not in contador_palavras.keys():
                    contador_palavras[palavra] = 1
                else:
                    contador_palavras[palavra] += 1
            palavras_repetidas = heapq.nlargest(50,contador_palavras, key=contador_palavras.get)
            return palavras_repetidas
                    
def tf(dataset):
    palavras_frequentes = repeticao_palavras(dataset)
    matriz_tf = {}
    for palavra in palavras_frequentes:
            documento_tf = []
            for dados in dataset:
                    frequencia = 0
                    for contador in nltk.word_tokenize(dados):
                            if contador == palavra:
                                frequencia += 1
                    palavra_tf = frequencia/len(nltk.word_tokenize(dados))
                    documento_tf.append(palavra_tf)
                    matriz_tf[palavra] = documento_tf
                    print (matriz_tf)
                    return matriz_tf
       
def idf(dataset):
    idfs_palavras = {}
    palavras_frequentes = repeticao_palavras(dataset)
    for palavra in palavras_frequentes:
        contador_documento = 0
        for dados in dataset:
                if palavra in nltk.word_tokenize(dados):
                    contador_documento += 1
    idfs_palavras[palavra] = np.log((len(dataset)/contador_documento)+1)
    print (idfs_palavras)
    return idfs_palavras

def tf_idf(dataset):
    tf1 = tf(dataset)
    idf1 = idf(dataset)
    matriz_tf_idf = []
    for palavra in tf1.keys():
        tf_idf = []
        for valor in tf1[palavra]:
            pontuacao = valor * idf1[palavra]
            tf_idf.append(pontuacao)
            matriz_tf_idf.append(tf_idf)
            print (matriz_tf_idf)

    
if login():
    search('Bolsonaro OR Lula')
    
    articles = driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')
    for i in range(50):
        
        tweet = driver.find_element(By.XPATH, '//div[@data-testid="tweetText"]').text
        tweets.append(tweet)

        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(6)

df = pd.DataFrame(zip(tweets),columns=['Tweets'])


df.to_csv(r".\tweets_scrapping.csv",index=False)

df.head()

df = pd.read_csv('.//tweets_scrapping.csv')
df = df.drop_duplicates()
print(df.head())

# limpeza_dados(df)
# repeticao_palavras(df)
# tf(df)
# idf(df)
tf_idf(df)

time.sleep(2)
driver.quit()
