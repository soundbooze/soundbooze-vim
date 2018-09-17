from ctypes import *

adder = CDLL('./adder.so')

res_int = adder.add_int(4,5)
print (res_int)

a = c_float(5.5)
b = c_float(4.1)

add_float = adder.add_float
add_float.restype = c_float
res_float = add_float(a, b)
print (res_float)
