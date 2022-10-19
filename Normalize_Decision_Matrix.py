import math
import pandas as pd

def r(m):
    list = []
    r = pd.DataFrame()  
    val = 0
    for i in range(len(m)):
        val = val + pow(m.iat[i,1] , 2)
    val = math.sqrt(val)
    for i in range(len(m)):
        list.append(m.iat[i,1]/val)
        r = pd.DataFrame(list)
    return r


from Centrality import *
def Normalize_decision_matrix(graph):
    df1 = degree_Centrality(graph)
    df2 = eigenvector_Centrality(graph)
    df3 = betweenness_Centrality(graph)
    df4 = closeness_Centrality(graph)
    
    df5 = r(df1)
    df6 = r(df2)
    df7 = r(df3)
    df8 = r(df4)
    
    data = [df5[0], df6[0], df7[0], df8[0]]
    headers = ["DC", "EC", "BC", "CC"]
    normalize_decision_matrix = pd.concat(data, axis=1, keys=headers)
    
    return normalize_decision_matrix

