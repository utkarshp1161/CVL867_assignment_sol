"""  Utility functions to compute correlation """
import numpy as np
import math

def compute_mean(lis):
    c = 0
    for i in lis:
        c += i
    return c/len(lis)


def compute_pearson(lis1, lis2):

    mean1 = compute_mean(lis1)
    mean2 = compute_mean(lis2)
    numerator = 0
    denominator1 = 0
    denominator2 = 0
    for i in range(len(lis1)):
        numerator += (lis1[i] - mean1)*(lis2[i] - mean2)
        denominator1 += (lis1[i] - mean1)**2
        denominator2 += (lis2[i] - mean2)**2
    
    return numerator/(math.sqrt(denominator1*denominator2))
        
def compute_spearman(lis1, lis2):
    def get_rank(x):
        """
        x: list
        Returns: list (rank of x)

        """
        rank_lis = np.argsort(x) + 1
        #print(rank_lis[::-1])
        return rank_lis[::-1]

    rank_lis1 = get_rank(lis1)
    rank_lis2 = get_rank(lis2)
    d_i_square = 0
    for i in range(len(rank_lis1)):
        d_i_square += (rank_lis1[i] - rank_lis2[i])**2
    
    spearman_corr = 1 - 6*(d_i_square/(len(lis1)*(len(lis1)**2 - 1)))

    return spearman_corr

