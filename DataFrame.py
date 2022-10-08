import pandas as pd
import re
import nltk

def limpeza_dados(dataset):
	# Para dividir um texto em frases *caso precise*: dataset = nltk.sent_tokenize(texto)
    # dataset = nltk.sent_tokenize(tweets)

    df_limpo = []
    auxiliar = " "

    for contador in range(len(dataset)):

        # Converte todas as palavras para minúsculo.
        auxiliar = dataset[contador].lower()
        
        # Converte tudo que não seja uma palavra (exemplo: Pontuação) para um espaço simples.
        auxiliar = re.sub(r'W', ' ', auxiliar)

        # Converte todas as quebras de linha para um espaço simples.
        auxiliar = re.sub(r'\r\n', ' ', auxiliar)

        # Inserção na lista limpa.
        df_limpo.append(auxiliar)
        
    return df_limpo

def cria_df():
    df = pd.read_csv('tweets_scrapping.csv')
    dfString = df['Tweets'].values.tolist()
    return limpeza_dados(dfString)
