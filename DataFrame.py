import pandas as pd
import re
import nltk
import Vetorizacao

def limpeza_dados(dataset, tweets):
	# Para dividir um texto em frases *caso precise*: dataset = nltk.sent_tokenize(texto)
    dataset = nltk.sent_tokenize(tweets)

    for contador in range(len(dataset)):
            # Converte todas as palavras para minúsculo.
            dataset[contador] = dataset[contador].lower()

            # Converte tudo que não seja uma palavra (exemplo: Pontuação) para um espaço simples.
            dataset[contador] = re.sub(r'W', ' ', dataset[contador])

            # Converte todas as quebras de linha para um espaço simples.
            dataset[contador] = re.sub(r's+', ' ', dataset[contador])

def cria_df(tweets):
    df = pd.DataFrame(zip(tweets),columns=['Tweets'])
    print(df.head())
    dfString = df['Tweets'].values.tolist()
    #limpeza_dados(dfString, tweets)
    df.to_csv(r".\tweets_scrapping.csv",index=False)
    df.head()
    Vetorizacao.repeticao(dfString)

