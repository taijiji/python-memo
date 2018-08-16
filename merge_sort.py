def merge_sort(array):
    if len(array) <= 1:
        return array
    
    middle = len(array) // 2

    left  = array[:middle]
    right = array[middle:]

    #print('middle  : ' + str(array[middle]))
    #print('left  : ' + str(left))
    #print('right : ' + str(right))

    left  = merge_sort(left)
    right = merge_sort(right)

    sorted_array = merge(left, right)
    print('merged: ' + str(sorted_array))

    return sorted_array


def merge(left, right):
    sorted_array = []
    left_i  = 0
    right_i = 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            sorted_array.append(left[left_i])
            left_i += 1
        elif left[left_i] > right[right_i]:
            sorted_array.append(right[right_i])
            right_i += 1
    
    if left_i >= len(left):
        sorted_array.extend(right[right_i:])
    
    if right_i >= len(right):
        sorted_array.extend(left[left_i:])
    
    return sorted_array


array = [3, 1, 10, 5, 2, 1, 5]
print('given_array : ' + str(array))
print('sorted_array: ' + str(merge_sort(array)))