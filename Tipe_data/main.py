# Tipe data: Angka satuan (Integer)
data_int = 10
print("Nilai data_int =",data_int ,"--Tipe data =",type(data_int))
# Tipe data: Angka dengan koma (Float)
data_float = 10.5
print("Nilai data_float =",data_float ,"--Tipe data =",type(data_float))
# Tipe data: Huruf (String)
data_str = "Hello World"
print("Nilai data_str =",data_str ,"--Tipe data =",type(data_str))
# Tipe data: Boolean
data_bool = True
print("Nilai data_bool =",data_bool ,"--Tipe data =",type(data_bool))

## Tipe data khusus

# Bilangan kompleks
data_complex = complex(5,6)
print("Nilai data_complex =",data_complex ,"--Tipe data =",type(data_complex))

# Tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print("Nilai data_c_double =",data_c_double ,"--Tipe data =",type(data_c_double))

# Tipe data dari bahasa C
from ctypes import c_float
data_c_float = c_float(10.5)
print("Nilai data_c_float =",data_c_float ,"--Tipe data =",type(data_c_float))

from math import sqrt
print("Nilai akar 9 =",sqrt(9))

from math import factorial
print("Nilai faktorial 5 =",factorial(5))
