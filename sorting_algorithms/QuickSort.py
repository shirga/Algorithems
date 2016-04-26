
def quick_sort (list, len):
    """
    This function sort a list of numbers, and count the number of compressions done by the algorithm
    
    This function sort list of numbers,
    the function implement the Quick sort algorithm,
    choosing a pivot element, using the help function choose_pivot and divide the 
    list to smaller then the pivot and bigger then the pivot. Then continue to sort each part recursively.

    :param list: the unsorted list
    :param len: the list length
    :return the sorted list, number of compressions done by the algorithems :
    """
 
    if (len == 1): 
        return list, 0
        
    comp = len - 1
    # Choose pivot and move him to the first place
    pivot_i = choose_pivot(list, len)
    list[0], list[pivot_i] = list[pivot_i], list[0]
    
    #partition part
    p = list[0]
    i = 1
    for j in range(1,len):
        if (list[j] < p):
            list[j], list[i] = list[i], list[j]
            i = i+1
    
    list[0], list[i-1] = list[i-1], list[0]
    pivot_place = i -1
    
    #print 'pivot = ', p, 'in place = ', pivot_place
    
    if (pivot_place > 0):    
        list[0:pivot_place], small_comp = quick_sort(list[0:pivot_place], pivot_place)
        comp = comp + small_comp
    if (pivot_place +1 < len):
        list[pivot_place+1:], big_comp = quick_sort(list[pivot_place+1:], len - pivot_place - 1)
        comp = comp +big_comp
    
    return list, comp
 
def choose_pivot(list, length):
    """
    This function choose a pivot from the list

    The function check the first, middle and last elements of the list, 
    and return the middle of there values (not the smallest and not the biggest)

    :param list: the unsorted list
    :param len: the list length
    :return the index of the pivot element :
    """

    middle = int((length -1)/2)
    if ( list[0]< max(list[middle], list[length -1]) and list[0] > min(list[middle], list[length -1]) ): 
        return 0
    elif ( list[middle]< max(list[0], list[length -1]) and list[middle] > min(list[0], list[length -1]) ):
        return middle
    else: 
        return length - 1


#%%
"""
This part use the function on an imput file with unsorted numbers
"""
unsorted = [5,12,6,8,2,45,67,3,9,-12,4,24,35]    
sorted, all_comp = quick_sort (unsorted, len(unsorted))
print 'sorted list = ', sorted, 'num of comperition = ', all_comp