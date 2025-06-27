# Casting
# Casting adalah mengubah tipe data ke tipe data lain
# Casting dilakukan dengan menggunakan fungsi int(), float(), str(), dll


# Integer
print("====Integer====")
data_int = 10
print("Nilai data_int =",data_int ,"--Tipe data =",type(data_int))
data_float = float(data_int)
print("Nilai data_float =",data_float ,"--Tipe data =",type(data_float))
data_str = str(data_int)
print("Nilai data_str =",data_str ,"--Tipe data =",type(data_str))
data_bool = bool(data_int)
print("Nilai data_bool =",data_bool ,"--Tipe data =",type(data_bool)) # Akan False jika angka integer 0


# Float
print("====Float====")
data_float = 10.5
print("Nilai data_float =",data_float ,"--Tipe data =",type(data_float))
data_int = int(data_float)
print("Nilai data_int =",data_int ,"--Tipe data =",type(data_int)) # Akan dibulatkan ke bawah
data_str = str(data_float)
print("Nilai data_str =",data_str ,"--Tipe data =",type(data_str))
data_bool = bool(data_float)
print("Nilai data_bool =",data_bool ,"--Tipe data =",type(data_bool)) # Akan False jika angka float 0


# String
print("====String====")
data_str = "10"
print("Nilai data_str =",data_str ,"--Tipe data =",type(data_str))
data_int = int(data_str)
print("Nilai data_int =",data_int ,"--Tipe data =",type(data_int)) # Akan error jika string bukan angka
data_float = float(data_str)
print("Nilai data_float =",data_float ,"--Tipe data =",type(data_float)) # Akan error jika string bukan angka
data_bool = bool(data_str)
print("Nilai data_bool =",data_bool ,"--Tipe data =",type(data_bool)) # Akan False jika string kosong


# Boolean
print("====Boolean====")
data_bool = True
print("Nilai data_bool =",data_bool ,"--Tipe data =",type(data_bool))
data_int = int(data_bool)
print("Nilai data_int =",data_int ,"--Tipe data =",type(data_int)) # Akan dibulatkan ke bawah
data_str = str(data_bool)
print("Nilai data_str =",data_str ,"--Tipe data =",type(data_str))
data_float = float(data_bool)
print("Nilai data_float =",data_float ,"--Tipe data =",type(data_float)) # Akan false jika angka float 0