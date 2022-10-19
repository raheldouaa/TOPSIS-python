
#from topsis import topsis

#import pandas as pd
#import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_edgelist('facebook_combined.txt', create_using=nx.Graph(), nodetype=int)



sp = nx.spring_layout(g)
plt.axis('off')
nx.draw_networkx(g, pos=sp, with_labels=False, node_size=35)
plt.show()

print ("average clustering : ",nx.cluster.average_clustering(g))

density = nx.density(g)
print("Network density:", density)

# connected return true or false
print("is connected : ", nx.is_connected(g))

print("diameter", nx.diameter(g))

transitivity = nx.transitivity(g)
print("transitivity: ", transitivity)

print (nx.info(g))





k = int(input("please type the value of K : "))

# # most influential
most_influential = nx.degree_centrality(g)
print("the top ",k," most influential")
sorted_result = sorted(most_influential, key=most_influential.get, reverse=True)
for i in sorted_result[:k]:
    print(i, most_influential[i])
    
    
# # most important connection
most_important_link = nx.eigenvector_centrality(g)
print("the top ",k," most important connection")
sorted_result = sorted(most_important_link, key=most_important_link.get, reverse=True)
for i in sorted_result[:k]:
    print(i, most_important_link[i])

# # best connecter
best_connecter = nx.betweenness_centrality(g)
print("the top ",k," most important connection")
sorted_result = sorted(best_connecter, key=best_connecter.get, reverse=True)
for i in sorted_result[:k]:
    print(i, best_connecter[i])

# closeness_centrality
closeness_centrality = nx.closeness_centrality(g)
print("the top ",k," most important connection")
sorted_result = sorted(closeness_centrality, key=closeness_centrality.get, reverse=True)
for i in sorted_result[:k]:
    print(i, closeness_centrality[i])
