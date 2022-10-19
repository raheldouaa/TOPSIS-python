import numpy as np

def Euclidean_Distance(positive_solutions, negative_solutions , normalize_decision_matrix):
    
    Negative_Si = (np.sum((negative_solutions-normalize_decision_matrix)**2, axis = 1))**0.5  
    Positive_Si = (np.sum((positive_solutions-normalize_decision_matrix)**2, axis = 1))**0.5

    # Calculate the relative closeness to the ideal solution:
    C = Negative_Si/(Negative_Si + Positive_Si)
    return (C)
