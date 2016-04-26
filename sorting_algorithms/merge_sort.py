
def margeSort (list):
    """
    This function sorts a list of numbers, and count the number of inversions done by the algorithm.
      
    This function sort list of numbers, the function implement the marge sort algorithm,
    dividing the list to two parts, sending thus lists to be sorted recursively and them marge the two parts in order.
      
    :param list: the unsorted list
    :return the sorted list, number of inversions done by the algorithms :
    """
    sorted = []
    n = len(list)
    if (n <= 1):
		return list, 0
    middle = int(n/2)
    left_list = list[0:middle]
    right_list = list[middle:]
	
    # send the two lists to sort
    left_sorted, left_inv = margeSort(left_list)
    right_sorted, right_inv = margeSort(right_list)
	
    #merge the two lists
    i = 0
    j = 0
    inv_count = left_inv + right_inv
    for k in range(0,n):
		if (j == len(right_sorted)):
			sorted.append(left_sorted[i])
			i = i+1
		elif (i == len(left_sorted)):
			sorted.append(right_sorted[j])
			j = j+1
		
		elif (left_sorted[i] < right_sorted[j]):
			sorted.append (left_sorted[i])
			i = i+1
		else:
			sorted.append(right_sorted[j])
			inv_count = inv_count + (len(left_sorted) - i)
			j = j+1
							
    return sorted, inv_count

 
unsorted = [5,12,6,8,2,45,67,3,9,-12,4,24,35]
sorted, inversions = margeSort(unsorted)
	
		
print  'final list = ', sorted, 'and inversions count = ', inversions