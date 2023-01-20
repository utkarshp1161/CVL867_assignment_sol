""" utility functions to sort a list of numbers"""
import time as time

def bubble_sort_lis(lis):
    """
    returns: list after sorting

    """

    if not list:
        raise ValueError("List is empty")

    time_start = time.time()
    for i in range(len(lis)): # no element right of lis[i] is smaller than lis[i] (at end of iteration)
        for j in range(len(lis) - i -1):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
    time_end = time.time()

    return lis, time_end - time_start

def merge_sort_lis(lis):
    """
    returns: list after sorting

    """
    if not list:
        raise ValueError("List is empty")

    
    time_start = time.time()
    def merge(lis, left_lis, right_lis):
        i = 0
        j = 0
        k = 0
        while i < len(left_lis) and j < len(right_lis):
            if left_lis[i] <= right_lis[j]:
                lis[k] = left_lis[i]
                i += 1
            else:
                lis[k] = right_lis[j]
                j += 1
            k += 1
        
        while i < len(left_lis):
            lis[k] = left_lis[i]
            i += 1
            k += 1

        while j < len(right_lis):
            lis[k] = right_lis[j]
            j += 1
            k += 1

        return lis

    if len(lis) >1:
        mid_index = int(len(lis)/2)

        left_lis = lis[: mid_index]
        right_lis = lis[mid_index :]

        merge_sort_lis(left_lis)
        merge_sort_lis(right_lis)
        lis = merge(lis, left_lis, right_lis)


    time_end = time.time()
    
    return lis, time_end - time_start

#def selection_sort()
def selection_sort_lis(lis):
    """
    returns: list after sorting

    """
    if not list:
        raise ValueError("List is empty")

    time_start = time.time()
    len_lis = len(lis)
   
    pos = 0
    while pos < len_lis:
        index_min = pos

        for i in range(pos + 1, len_lis):
            if  lis[index_min] > lis[i]:
                index_min = i
        
        lis[pos], lis[index_min] = lis[index_min], lis[pos]
        pos +=1

    time_end = time.time()

    return lis, time_end - time_start

