from Centrality import *

def Decision_Matrix (g):
    DC = degree_Centrality(g)
    EC = eigenvector_Centrality(g)
    BC = betweenness_Centrality(g)
    CC = closeness_Centrality(g)

    data = [DC[1], EC[1], BC[1], CC[1]]
    headers = ["DC", "EC", "BC", "CC"]
    decision_matrix = pd.concat(data, axis=1, keys=headers)
    
    return decision_matrix
