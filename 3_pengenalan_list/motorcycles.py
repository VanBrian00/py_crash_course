motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#mengganti elemen pertama di dalam list.
#dari honda jadi ducati.
motorcycles[0] = 'ducati'
print(motorcycles)

#semua nilai yang ada di dalam list dapat kita ubah.
#dengan cara yang sama seperti di atas.

motorcycles.append('honda')
print(motorcycles)

#di atas untuk menambahkan data/elemen ke dalam list.
#data/elemen yang ditambahkan akan masuk ke bagian belakang.

#gunakan insert jika ingin menambahkan di posisi mana pun.
#di bawah ini akan menambahkan ke posisi ke 2.
motorcycles.insert(1, 'kawasaki')
print(motorcycles)

#menghapus elemen di dalam list bisa dengan del,
#jika tahu posisinya.

del motorcycles[1]
print(motorcycles)

#setelah data dihapus, data tidak akan muncul lagi 
#di pemanggilan list berikutnya setelah del.

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#pop di pake untuk menghapus nilai/ elemen paling belakang
#dan kita masukkan ke dalam variabel khusus untuk 
#elemen yang sudah kita hapus.
#agar data lainnya dapat dipakai ulang

motorcycles.remove('yamaha')
print(motorcycles)

#pakai remove jika tidak tahu posisi dan hanya tahu nilai
#dengan begitu kita bisa hapus nilai yang kita tahu.
#seperti contoh di atas
#remove hanya menghapus 1 nilai,
#jika ada lebih dari 1 nilai yang sama harus pakai loop
#untuk hapus semuanya dengan nilai sama.
