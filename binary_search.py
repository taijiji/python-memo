def binary_search(list, target):
    if not target:
        return "Error: target is None"
    
    if not list:
        return "Error: list is None"

    result = False
    low = 0
    high = len(list) -1

    while low <= high:
        mid = ( low + high ) // 2
        
        print('target:' + str(target))
        print('low : ' + str(list[low]))
        print('high: ' + str(list[high]))
        print('mid : ' + str(list[mid]))

        if target == list[mid]:
            result = True
            break
        elif target < list[mid]:
            high = mid - 1
        elif target > list[mid]:
            low = mid + 1

    return result
        
list = [1,5,4,3,6,10,2]
sorted_list = sorted(list)
target = 3
print("original: " + str(list))
print("sorted  : " + str(sorted_list))
print("result  : " + str(binary_search(sorted_list, target)))

# sorted : O(n^2) or O(n log n)
# binary search: log(n)

# Total: log(n) < O(n log n) = O(n log n)