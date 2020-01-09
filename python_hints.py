def decimal2binary(n):
    n =  int(n)
    if n:
        return decimal2binary(n//2) + str(n%2)
    return ''
def dec2oct(n):
    n = int(n)
    if n:
        return dec2oct(n//8) + str(n%8)
    return ''
print(ord('a'))
print(chr(97))
'''
97
a
'''

print(int('10',2))
print(int('17',8))
print(int('1A',16))

'''
2
15
26
'''

print(bin(2))
print(oct(15))
print(hex(26))
'''
0b10
0o17
0x1a
'''

print(decimal2binary('2'))
print(dec2oct('15'))
'''
10
17
'''
