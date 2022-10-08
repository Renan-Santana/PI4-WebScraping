import pandas as pd
import heapq
import numpy as np
import nltk

def repeticao_palavras(dfString):
	contador_palavras = {}
 
	for dados in dfString:
            # dados = dfString[dados]
            palavras_tokenizadas = nltk.word_tokenize(dados)
            for palavra in palavras_tokenizadas:
                if palavra not in contador_palavras.keys():
                    contador_palavras[palavra] = 1
                else:
                    contador_palavras[palavra] += 1
            palavras_repetidas = heapq.nlargest(50,contador_palavras, key=contador_palavras.get)
            return palavras_repetidas

def tf(dfString):
    palavras_frequentes = repeticao_palavras(dfString)
    matriz_tf = {}
    for palavra in palavras_frequentes:
            documento_tf = []
            for dados2 in dfString:
                    frequencia = 0
                    palavras_tokenizadas = nltk.word_tokenize(dados2)
                    for contador in palavras_tokenizadas:
                            if contador == palavra:
                                frequencia += 1
                    palavra_tf = frequencia/len(nltk.word_tokenize(dados2))
                    documento_tf.append(palavra_tf)
                    matriz_tf[palavra] = documento_tf
                    print (matriz_tf)
                    return matriz_tf
       
def idf(dfString):
    idfs_palavras = {}
    palavras_frequentes = repeticao_palavras(dfString)
    for palavra in palavras_frequentes:
        for dados in dfString:
                contador_documento = 0
                palavras_tokenizadas = nltk.word_tokenize(dados)
                for contador in palavras_tokenizadas:
                    if contador == palavra:
                        contador_documento += 1
    idfs_palavras[palavra] = np.log((len(dfString)/contador_documento)+1)
    print (idfs_palavras)
    return idfs_palavras

def tf_idf(dfString):
    tf1 = tf(dfString)
    idf1 = idf(dfString)
    matriz_tf_idf = []
    for palavra in tf1.keys():
        tf_idf = []
        for valor in tf1[palavra]:
            pontuacao = valor * idf1[palavra]
            tf_idf.append(pontuacao)
            matriz_tf_idf.append(tf_idf)
            print (matriz_tf_idf)

def repeticao (dfString):
    print(tf(dfString))