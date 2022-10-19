
import matplotlib.pyplot as plt

#from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

import networkx as nx

g = nx.read_edgelist('facebook_combined.txt', create_using=nx.Graph(), nodetype=int)

from Decision_matrix import *
data = Decision_Matrix(g)

# number of clusters
k_max = int(input("enter K max : "))
from Optimal_k_value import optimal_k_value
optimal_k_value(data, k_max)

# applying k means clusters
number_clusters = int(input("enter number of clusters : "))
kmeans = KMeans(n_clusters = number_clusters)
kmeans.fit(data)

data['kmeans'] = kmeans.labels_

# plotting the result
plt.scatter(x=data, y = data, c=data['kmeans'])
plt.show()
