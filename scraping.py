# Realizar as instalações das libs abaixo
# pip install requests
# pip install pandas
# pip install beautifulsoup4
# pip install selenium

import time
import requests
import pandas as pd
import json

from bs4 import BeautifulSoup
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# leitura dos dados do json

with open("credenciais.json", encoding='utf-8') as jsonCredenciais:
    credenciais = json.load(jsonCredenciais)

# url da página de login do twitter
urlTwitter = "https://twitter.com/i/flow/login"

# instacia do firefox
options = Options()
options.headless = True # exibe o navegador
service = Service(executable_path = "geckodriver-v0.31.0-win64\geckodriver.exe")

driver = webdriver.Firefox(service = service)

driver.get(urlTwitter)

xPathEmail = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"
xPathAvancar = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div"
xPathSenha = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
xPathEntrar = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div"

time.sleep(10)
try:
    
    driver.find_element(By.XPATH, xPathEmail).send_keys(credenciais['email'])
    time.sleep(5)
    
    driver.find_element(By.XPATH, xPathAvancar).click()
    time.sleep(5)
    
    driver.find_element(By.XPATH, xPathSenha).send_keys(credenciais['senha'])
    time.sleep(5)
    
    driver.find_element(By.XPATH, xPathEntrar).click()
    time.sleep(10)
    
    print("logado com sucesso!")
except Exception as e:
    driver.quit()
    print(e)

driver.quit()
