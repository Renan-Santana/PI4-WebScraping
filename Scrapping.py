import csv
import json
import os
import time
import numpy as np
import pandas as pd
import requests
import DataFrame
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from sklearn.feature_extraction.text import (CountVectorizer, TfidfTransformer, TfidfVectorizer)

# Função para verificar se o elemento existe na DOM.
def elemento_presente(como, oque):

    try:
        driver.find_element(by = como, value = oque)
    
    except NoSuchElementException as excessao:
        return False
    
    return True


# Leitura dos dados do JSON.
with open("credenciais.json", encoding='utf-8') as jsonCredenciais:
    credenciais = json.load(jsonCredenciais)

# URL da página de login do Twitter.
url_twitter = "https://twitter.com/i/flow/login"

# Cria uma nova instância do Firefox.
opcoes = Options()
opcoes.headless = True  # Exibe o navegador.

# Executável do Geckodriver.
servico = Service(executable_path="geckodriver-v0.31.0-win64\geckodriver.exe")
driver = webdriver.Firefox(service=servico)

tweets = []

# Abre uma nova página.
driver.get(url_twitter)


def login():

    # Atribuição de valores da primeira tela.
    xpath_email = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"
    xpath_avancar = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div"

    # Atribuição de valores da segunda tela.
    xpath_valida_nomecelular = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input"
    xpath_avancarusuario = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div"

    # Atribuição de valores da terceira tela.
    xpath_senha = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
    xpath_entrar = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div"

    time.sleep(3)

    # Inicia um novo login.
    try:

        driver.find_element(By.XPATH, xpath_email).send_keys(credenciais['email'])
        time.sleep(2)

        driver.find_element(By.XPATH, xpath_avancar).click()
        time.sleep(2)

        # Verifica se o elemento de verificação de usuario existe.
        if elemento_presente('xpath', xpath_valida_nomecelular):

            driver.find_element(By.XPATH, xpath_valida_nomecelular).send_keys(credenciais['nome'])
            time.sleep(2)

            driver.find_element(By.XPATH, xpath_avancarusuario).click()
            time.sleep(2)

        driver.find_element(By.XPATH, xpath_senha).send_keys(credenciais['senha'])
        time.sleep(2)

        driver.find_element(By.XPATH, xpath_entrar).click()
        time.sleep(2)

    except Exception as excessao:

        driver.quit()
        print(excessao)
        return False

    return True


def search(nome):

    # Atribuição de valores.
    xpath_pesquisa_twitter = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input"
    xpath_lasted = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div/span"

    try:

        driver.find_element(By.XPATH, xpath_pesquisa_twitter).send_keys(nome)
        time.sleep(2)

        driver.find_element(By.XPATH, xpath_pesquisa_twitter).send_keys(Keys.ENTER)
        time.sleep(2)

        driver.find_element(By.XPATH, XPathLasted).click()
        time.sleep(2)
    except Exception as e:
        driver.quit()
        print(e)
    
if login():
    search('Eleições 2022 OR Eleições OR Eleicoes OR PT OR PL OR PDT OR Jair OR Bolsonaro OR Lula OR PDT OR Ciro OR MDB OR Simone OR Simone Tebet OR Tebet OR Padre Kelmon OR NOVO OR Felipe Avila')
    
    articles = driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')
    for i in range(100_000):
        
        tweet = driver.find_element(By.XPATH, '//div[@data-testid="tweetText"]').text
        tweets.append(tweet)

        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(4)

dataframe = pd.DataFrame(zip(tweets), columns = ['Tweets'])
dataframe.to_csv(r".\tweets_scrapping.csv", inde = False)

time.sleep(2)
driver.quit()
