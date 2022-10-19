#import numpy as np
import pandas as pd

def Weight_matrice(matrix , w):
    list = matrix.to_numpy()
    res = list @ w
    df = pd.DataFrame(res)
    return df
