# importação de libs que serão utilizadas
# pip install pandas
# pip install numpy
# pip install matplotlib
# pip install sklearn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from scipy.spatial.distance import cdist, pdist
from sklearn.metrics import silhouette_score
from sklearn.semi_supervised import LabelSpreading

# Pré processamento dos dados
dataset_vetorizado = pd.read_csv('tweets_scrapping.csv', #passar path correto do dataset_vetorizado.csv
                                #delimiter = ';', 
                                low_memory = False)

dataset_vetorizado.info()

if dataset_vetorizado.isnull().values.any():
    dataset_vetorizado.dropna(inplace = True)


tweets_array = dataset_vetorizado.values

# KMeans
k_means = KMeans(n_clusters = 3).fit(tweets_array)

# Metricas
centroids = k_means.cluster_centers # ajustando centroids

k_euclid = [cdist(tweets_array, cent, 'euclidean') for cent in centroids] # calculando a distandcia euclidiana de cada ponto dado o centroid
dist = [np.min(k, axis = 1) for k in k_euclid]

soma_quadrado_clusters = [sum(d**2 for d in dist)] # soma dos quadrados das distancias

soma_total = sum(pdist(tweets_array)**2)/tweets_array.shape[0] # soma toal dos quadrados

soma_quadrado_entre_clusters = soma_total - soma_quadrado_entre_clusters # soma dos quadrados entre os cluster

# Curva de Elbow
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(3, soma_quadrado_entre_clusters/soma_total * 100, 'b*-')
ax.set_ylim((0,100))
plt.grid(True)

# Silhouette Score
labels = k_means.labels_

score = silhouette_score(tweets_array, labels, metric = 'euclidean')

print('Score da Silhouette Score: ', score)


# Fazendo mapeamento do cluster no dataset
dataset_clusters = pd.DataFrame(dataset_vetorizado, columns = ['Tweets'])
dataset_clusters['Cluster'] = labels

# Gerando csv dos tweets e seus respectivos cluster
dataset_clusters.to_csv('tweets_clusters.csv', index = True)


