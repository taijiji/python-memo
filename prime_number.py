
def get_prime_number(num):
    print(num)
    is_prime = 0
    if num > 0:
        for i in range(2, num):
            result = num % i
            #print("num: %s, i: %s , result: %s" % (num, i, result))
            if num % i == 0:
                is_prime += 1
    elif num == 0:
        pass
    elif num < 0:
        pass

    if is_prime == 0:
         return True
    else:
         return False

print(get_prime_number(5))
print(get_prime_number(6))
print(get_prime_number(9))
print(get_prime_number(11))
print(get_prime_number(13))

