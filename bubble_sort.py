a = [1, 10, 5, 2, 1, 5]

def bubble_sort(array):
	n = len(array)
	for j in range(n-1, 0, -1):
		print('j = %d' %j)
		#print('array = %d' % array[j])

		for i in range(0, j, +1):
			if array[i+1] < array[i]:
				print('i = %d' % i)
				#print('array = %d' % array[i])
				temp = array[i]
				array[i] = array[i+1]
				array[i+1] = temp
				print("current array : %s" % array)
	return array

print(a)
print(bubble_sort(a))
