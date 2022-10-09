import pandas as pd
import numpy as np
import DataFrame

def idf (tweets_limpos):
    
    contador_palavras_global = {}
    resultado_idf = {}
    lista_artigos = ['o', 'os', 'ao', 'aos', 'do', 'dos', 'no', 'nos', 'pelo', 'pelos', 'a', 'as',
    'à', 'às', 'da', 'das', 'na', 'nas', 'pela', 'pelas', 'um', 'uns', 'dum', 'duns', 'num', 'nuns',
    'uma', 'umas', 'duma', 'dumas', 'numa', 'numas', 'para', 'ou', 'e', 'de', 'no', 'que', 'com', 'em',
    'é', 'ó', 'ô', 'tá']

    for tweet in tweets_limpos:
    
        palavras_tweet = tweet.split()
        for palavra in palavras_tweet:
    
            if palavra not in lista_artigos:

                if palavra not in contador_palavras_global.keys():
                    contador_palavras_global[palavra] = 1
                else:
                    contador_palavras_global[palavra] += 1
        
# IDF = log(N/n), em que "N" é o número total de documentos e "n" é o número onde o termo apareceu.
    for palavra in contador_palavras_global:

        resultado_idf[palavra] = np.log(len(tweets_limpos)/contador_palavras_global.get(palavra))

    return resultado_idf

tweets_limpos = DataFrame.cria_df()
resultado_idf = idf(tweets_limpos)

for resultado in resultado_idf:
    print(f"{resultado}: {resultado_idf.get(resultado)}")