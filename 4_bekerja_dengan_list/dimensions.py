dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

test_tuple = (1,)
#harus ada tanda koma di belakang nilai pertama
#sebuah tuple, meski cuman 1 nilai.
print(test_tuple[0])

test_tuple_2 = 1, 2
#aslinya tuple bukan karena tanda kurung ()
#tapi dari tanda koma. pakai tanda kurung agar
#lebih rapi saja.
print(test_tuple_2[0])
print(test_tuple_2[1])

print("\nDimensions awal:")
for dimension in dimensions:
    print(dimension)
    
#kita bisa ubah isi tuple dengan
#membuat ulang tuple tersebut.

dimensions = (400, 100)
print("\nDimensions setelah diubah:")
for dimension in dimensions:
    print(dimension)
    
#pakai tuple jika kamu tidak ingin datanya
#diubah selama program berjalan.