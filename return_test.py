def stupid_func(array):
    for i in range(len(array)):
        if i == 2:
            return 'Finished: i == 1'
        
        print(array[i])
    
    return 'Finished: i == len(array)'

array = [1,2,3,4,5]

print(stupid_func(array))