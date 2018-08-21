def linear_search(list, target):
    result = False

    if not target:
        return "Error: target is None"
    
    if not list:
        return "Error: list is None"

    for n in list:
        if n == target:
            result = True
            return result

    return result    


list = [1,5,2,3,6,10,2]
target = 1
print("original: " + str(list))
print("result  : " + str(linear_search(list, target)))

# O(N)