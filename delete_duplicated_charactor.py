def reverse_char(char):
    if char == None:
        return None
    elif len(char) == 1:
        return char
    else:
        for i in range(len(char)-2):
            for j in range(i+1, len(char)-2):

                #print('i: %d' % i)
                #print('j: %d' % j)

                if char[i] == char[j]:
                    if j == ( len(char)-1) :
                        char = char[:-1]
                    else:
                        #print('char: %s' % char)
                        #print('char[i]: %s' % char[i])
                        #print('char[j]: %s' % char[j])

                        #print('char[:j]: %s' % char[:j])
                        #print('char[j+1:]: %s' % char[j+1:])

                        char = char[:j] + char[j+1:]                    

                #print('char: %s' % char)
                #print('len(char): %s' % len(char))

        return char

char = 'abcdabef'
print('Source: ' + char)
print('Reversed: ' + reverse_char(char))

char = 'abcdabefff'
print('Source: ' + char)
print('Reversed: ' + reverse_char(char))

char = 'a'
print('Source: ' + char)
print('Reversed: ' + reverse_char(char))

char = None
print('Source: ' + str(char))
print('Reversed: ' + str(reverse_char(char)))

char = 'abcd'
print('Source: ' + char)
print('Reversed: ' + reverse_char(char))

char = 'aaaa'
print('Source: ' + char)
print('Reversed: ' + reverse_char(char))

char = 'aaaabbbb'
print('Source: ' + char)
print('Reversed: ' + reverse_char(char))