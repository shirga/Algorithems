
file_name = 'QuickSort.txt'

try:
    fh  = open(file_name)
except:
	print 'file name is wrong'

unsorted= []
for line in fh:
	num = line.rstrip()
	num = int(num)
	unsorted.append(num)

def quick_sort (list, len):
	#print 'got list ', list, 'with len', len
	if (len == 1): 
		return list, 0
		
	comp = len - 1
	# Choose pivot and put hom in the first place
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
	temp = []
	#return length -1
	#return 0
	middle = int((length -1)/2)
	temp = [list[0], list[middle], list[length -1]]
	#print ' fist = ', temp[0], 'middle = ', temp[1], 'last = ', temp[2]
	temp = sorted(temp)
	if (temp[1] == list[0]): 
		return 0
	elif (temp[1] == list[middle]):
		return middle
	else: 
		return length - 1
	
sorted, all_comp = quick_sort (unsorted, len(unsorted))
print 'sorted list = ', sorted, 'num of comperition = ', all_comp