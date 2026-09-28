for value in range(6):
	print(value)

#range itu untuk perulangan dengan angka
#jika ada dua angka contoh: range(2, 6)
#artinya mulai dari angka 2 berakhir sebelum 6
#jika hanya 1 angka artinya harus mulai dari 0
#berakhir sebelum angka tersebut.

numbers = list(range(1, 11))
print(numbers)

# di atas adalah contoh menggunakan fungsi range untuk
#memasukkan angka ke dalam sebuah list.
#ketika di print isi listnya adalah angka.

for value in range(1, 6, 3):
	print(value ** 2)

#contoh di atas adalah menambahkan angka ke 3 di dalam range
#angka tersebut artinya setiap 1 angka yang telah keluar,
#angka berikutnya yang akan keluar adalah angka yang telah
#ditambahkan angka n (angka yang ke 3 dalam kurung range)
# ** 2 artinya pangkat dua, jadi hasilnya nilai dari n^2

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#min untuk menampilkan nilai minimal
#max untuk menampilkan nilai maximal
#sum untuk menampilkan jumlah seluruh angka