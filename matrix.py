# import library
import numpy as np
import pandas as pd

# Belajar Numpy array
panjang =[4,5,6]
lebar = [3,4,5]
print (type(panjang))
# ubah ke numpy array
panjang_arr = np.array([panjang])
panjang_arr
lebar_arr = np.array([lebar])
lebar_arr
# Menghitung Luas
luas = panjang_arr*lebar_arr
print (f'Luas yang di dapat adalah {luas}')

# menghitung Keliling
keliing = 2*(panjang_arr*lebar_arr)
print(f'Keliling yang didapat adalah{keliing}')

# cara mau menghitung luas tanpa ubah ke array
luas = [p * l for p,l in zip(panjang, lebar)]
print(luas)

# cara mau menghitung keliling tanpa ubah ke array
keliling = [2*(p + l) for p,l in zip(panjang, lebar)]
print(keliling)

deret =list(range(12))
print(deret)
deret_array = np.array(deret)
print(deret_array)
# penjummlahan dengan numpy array
print(deret_array.sum())

matrix = deret_array.reshape(2,6)
print(matrix)

tensor = deret_array.reshape(3,2,2)
print(tensor)

print(tensor.sum(axis=2))

tensor2 = deret_array.reshape(2,2,3)
print(tensor2)

#penjumlahan perbaris
print(matrix.sum(axis=1))

# penjumlahan perkolom
print(matrix.sum(axis=0))
