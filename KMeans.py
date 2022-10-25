# importação de libs que serão utilizadas

import pandas as pd
from sklearn.cluster import KMeans

# Pré processamento dos dados
dataset_vetorizado = pd.read_csv('vetorizacao_tf_idf.csv', #passar path correto do dataset_vetorizado.csv
                                #delimiter = ';', 
                                low_memory = False)

dataset_vetorizado.info()

if dataset_vetorizado.isnull().values.any():
    dataset_vetorizado.dropna(inplace = True)


tweets_array = dataset_vetorizado.values

# KMeans
k_means = KMeans(n_clusters = 3).fit(tweets_array)

labels = k_means.labels_

# Fazendo mapeamento do cluster no dataset
dataset_vetorizado_clusters = pd.DataFrame(dataset_vetorizado)
dataset_vetorizado_clusters['Cluster'] = labels

dataset_tweets_clusters = pd.read_csv('tweets_scrapping.csv')
dataset_tweets_clusters['Cluster'] = labels

# Gerando csv dos tweets e seus respectivos cluster
dataset_vetorizado_clusters.to_csv('tweets_vetorizados_agrupados.csv', index = True)
dataset_tweets_clusters.to_csv('tweets_texto_agrupados.csv', index = True)


