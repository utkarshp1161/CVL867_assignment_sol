import numpy as np

def rng_usual(seed, n):
    """Returns array with n random numbers b/w 0 and 1
    
    """
    np.random.seed(seed)
    rand_array = np.random.uniform(0, 1, n)

    return rand_array


def rng_pm(a = 7**5, seed = 362355, m = 2**31 -1 , n = 1000, period_flag = False):
    """Returns period of park and miller 
    Args:
        a: int
        l0: int
        m: int
        n: int

    
    Returns: array 
    """
    if period_flag:
        rand_array = np.ones(shape = (n))
        for index in range(n):
            temp = (a*seed) % m
            if temp in rand_array:
                return index
            rand_array[index] = temp
            seed = temp

    else:
        rand_array = np.ones(shape = (n))
        for index in range(n):
            temp = (a*seed) % m
            rand_array[index] = temp
            seed = temp

    
    return rand_array


