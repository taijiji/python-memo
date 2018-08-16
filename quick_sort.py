
def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    left = []
    right = []
    for i in range(1, len(array)):
        if array[i] <= pivot:
            left.append(array[i])
        elif array[i] > pivot:
            right.append(array[i])

    print('left : ' + str(left))
    print('right : ' + str(right))

    left  = quick_sort(left)
    right = quick_sort(right)

    sorted_array = left + [pivot] + right

    return sorted_array

array = [3, 10, 5, 2, 1, 5, 6]
print('given_array : ' + str(array))
print('sorted_array: ' + str(quick_sort(array)))