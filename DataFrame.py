import pandas as pd
import re
import nltk

def limpeza_dados(dataset):

    dataframe_limpo = []
    auxiliar = " "

    for contador in range(len(dataset)):

        # Converte todas as palavras para minúsculo.
        auxiliar = dataset[contador].lower()
        
        # Converte tudo que não seja uma palavra (exemplo: Pontuação) para um espaço simples.
        auxiliar = re.sub(r'W', ' ', auxiliar)

        # Converte todas as quebras de linha para um espaço simples.
        auxiliar = re.sub(r'\r\n', ' ', auxiliar)

        # Converte todos os caracteres especiais para um espaço simples.
        caracteres_especiais = [';', ':', '!', '?', '*', '.', ',', '@', '#', '$', '(', ')', '[', ']', '{','}']
        for caracter in caracteres_especiais: 
            auxiliar = auxiliar.replace(caracter, ' ')

        # Inserção na lista limpa.
        dataframe_limpo.append(auxiliar)
        
    return dataframe_limpo

def cria_df():

    dataframe = pd.read_csv('tweets_scrapping.csv')
    dataframe_string = dataframe['Tweets'].values.tolist()
    return limpeza_dados(dataframe_string)
