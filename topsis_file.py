
#import pandas as pd
import networkx as nx

from Normalize_Decision_Matrix import *
from Weighted_Decision_Matrix import *
from Euclidean_Distance import *

graph = nx.read_edgelist('facebook_combined.txt', create_using=nx.Graph(), nodetype=int)

#  decision matrix
from Decision_matrix import *
decision_matrix = Decision_Matrix(graph)

# Normalize_Decision_Matrix
normalize_decision_matrix = Normalize_decision_matrix(graph)

#  weighted decision matrix
weights =[0.2 , 0.2 , 0.3 , 0.3] 

weighted_decision_matrix =  Weight_matrice(normalize_decision_matrix , weights)

# Determine the positive ideal and negative ideal solutions.
criterias = [1, 1, 1, 1]
from Ideal_Solution import Ideal_Solution
ideal_solution = Ideal_Solution(weighted_decision_matrix, criterias)

Positive_Ideal_Solutions = ideal_solution[0] 
Negative_Ideal_Solutions = ideal_solution[1]
# Euclidean distance
relative_closeness_ideal_solution = Euclidean_Distance(Positive_Ideal_Solutions, Negative_Ideal_Solutions, normalize_decision_matrix)
