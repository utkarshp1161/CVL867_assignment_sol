""" utils. for finding largest value in a list"""
import time as time

def max_value_algo1(lis):
    time_start = time.time()
    max_val = lis[0]
    for i in lis:
        if i > max_val:
            max_val = i

    time_end = time.time()
    
    return max_val, time_end - time_start

def max_value_algo2(lis):
    time_start = time.time()
    #def last_element_sort_lis(lis):
    for i in range(len(lis)): # no element right of lis[i] is smaller than lis[i] (at end of iteration)
        for j in range(len(lis) - i -1):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
    

    time_end = time.time()
    
    return lis[-1], time_end - time_start





