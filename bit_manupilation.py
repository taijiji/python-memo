
# binary number : add '0b'
a_binary = 0b0101
print(a_binary) # 5

# to convert to binary from decimal : 'bin()'
a_decimal = 5
print( bin(a_decimal) ) # 0b101 


# hexadicimal number : add '0x'
a_hex = 0x20
print(a_hex) # 32

# to convert to hexadicimal from binary : 'hex()'
a_binary = 0b0101
print( hex(a_binary)  ) # 0x05

# to convert to hexadicimal from decimal : 'hex()'
a = 32
print( hex(a) ) # 0x20


# shift 1 bit to left: "<< 1"
a_binary = 0b0101
print( bin(a_binary << 1)  ) # 0b1010

a = 5 
print( bin(a << 1)  ) # 0b1010

# shift 1 bit to right: ">> 1"

a_binary = 0b0101
print( bin(a_binary >> 1)  ) # 0b10 (= 0b0010)


# OR : "|"
print (0|1) # 1
print (0|0) # 0
print (0|0|1) # 1
print ( bin( 0b0001 | 0b1000 | 0b1100) ) # 0b1101


# AND: "&"
print (0&1) # 0
print (1&1) # 1
print (0&0&1) # 0
print ( bin( 0b1001 & 0b1000 & 0b1100) ) # 0b1000

# XOR: "^"
print (0^1) # 1
print (0^0) # 0
print (0^0^1) # 1
print ( bin( 0b0001 ^ 0b1001 ) ) # 0b1000
 
# NOT : "~"
print( bin(~0b01) ) # -0b10
