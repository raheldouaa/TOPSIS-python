import pandas as pd
import networkx as nx


def closeness_Centrality(graph):
    closeness_centrality = nx.closeness_centrality(graph)
    closeness_centrality = pd.DataFrame.from_dict(closeness_centrality.items())
    return closeness_centrality

def degree_Centrality(graph):
    degree_centrality = nx.degree_centrality(graph)
    degree_centrality = pd.DataFrame.from_dict(degree_centrality.items())
    return degree_centrality

def eigenvector_Centrality(graph):
    most_important_link = nx.eigenvector_centrality(graph)
    most_important_link = pd.DataFrame.from_dict(most_important_link.items())
    return most_important_link

def betweenness_Centrality(graph):
    best_connecter = nx.betweenness_centrality(graph)
    best_connecter = pd.DataFrame.from_dict(best_connecter.items())
    return best_connecter

