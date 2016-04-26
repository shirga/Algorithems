"""
These functions are used to keep the median element from a stream of numbers, 
here represented by a list on numbers using heaps.

The function medianMaintenance always keep the median and also keeps the sum of 
all the medians whenever a new number is added.
The two other functions are helper functions to keep the heaps leveled. 
"""
import heapq

def make_heaps_even(low_size, high_size, heap_low, heap_high):
    """
    This function keeps the heaps even, the difference in the heaps size can't be more than one
    
    :param low_size: the size of the low heap
    :param high_size: the size of the high heap
    :param heap_low: heap that store all the elements that are smaller then the median
    :param heap_high: heap that store all the elements that are bigger than the median
    
    :return low_size, high_size: the updated size of the heaps
    """
    if(low_size > high_size +1):
        move_num = heapq.heappop(heap_low)
        heapq.heappush(heap_high, -move_num)
        low_size -= 1
        high_size += 1
        #print 'moving', -move_num, 'from low to high heap'
    if (high_size > low_size +1):
        move_num = heapq.heappop(heap_high)
        heapq.heappush(heap_low, -move_num)
        high_size -= 1
        low_size += 1
        #print 'moving', move_num, 'from high to low heap'
    return low_size, high_size
        
def get_median(low_size, high_size, heap_low, heap_high):
    """
    This function returns the median element, 
    if the low heap is bigger then the median is the biggest in the heap and 
    the function will return it.
    if the high heap is bigger then the median is the smallest element in that 
    heap and we will return it.
    if the heaps are equals that we will return the biggest element from the low heap
    
    :param low_size: the size of the low heap
    :param high_size: the size of the high heap
    :param heap_low: heap that store all the elements that are smaller then the median
    :param heap_high: heap that store all the elements that are bigger than the median
    
    :return median: the median element from the heaps
    """
    if(low_size < high_size):
        temp_median = heapq.heappop(heap_high)
        heapq.heappush(heap_high,temp_median)
        #print 'high is bigger, median is ', temp_median      
        return temp_median
    else:
        temp_median = heapq.heappop(heap_low)
        heapq.heappush(heap_low,temp_median)
        #print 'low is bigger or equal, median is ', temp_median      
        return -temp_median

def medianMaintnance(numbers_list):
    """
    This function returns the sum of all the median elements,
    when colculating the median after each element is added.
    
    the function uses 2 heaps:
    high heap - keeps all the numbers that are bigger that the median, 
    and can return in O(1) time the smallest number. regulr heap from heapq
    low heap - - keeps all the numbers that are smaller that the median, 
    and can return in O(1) time the biggest number. 
    put all the numbers with negetive value in a heap from heapq
    
    
    :param numbers_list: a list of numbers    
    :return median_sum: the sum of all the medians element over time
    """
    heap_low = []
    heap_high = []
    median = 0
    median_sum = 0
    h_low_size = 0
    h_high_size = 0   

    for num in numbers_list:
        #print num
        if(num < median):
            # push to low heap'
            heapq.heappush(heap_low,-num)
            h_low_size += 1
        else:
            # push to high heap'
            heapq.heappush(heap_high, num)
            h_high_size+=1
            
        # make heaps even and get the new median
        h_low_size, h_high_size = make_heaps_even(h_low_size, h_high_size, heap_low, heap_high)
        median = get_median(h_low_size, h_high_size, heap_low, heap_high)
        #print 'median = ', median
        median_sum += median
        
    return median_sum
    
numbers_list = [1369,831,5283,1477,3932,2632,5179,1645,5714,1183,982,6846,4154,1595,5426,6412,9160,1746,3382,8375,8279,1500]
print medianMaintnance(numbers_list)
        
