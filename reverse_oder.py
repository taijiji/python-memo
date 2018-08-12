s = 'abcde'

print(s)

s_reversed = ''
for i in range(len(s)-1, -1, -1):
    print(i)
    s_reversed += s[i]

print(s_reversed) 

