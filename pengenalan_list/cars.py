#sort() merupakan metode untuk mengurutkan sebuah list.

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#setelah pakai sort, urutan di list akan berubah dan
#tidak akan kembali lagi seperti sebelumnya.
#contoh di atas untuk mengurutkan elemen di list berdasarkan
#alfabet.

#untuk membalikkan urutannya bisa pakai
#reverse = true, di dalam tanda kurung sort

cars.sort(reverse=True)
print(cars)

#tidak boleh ada spasi di reverse hingga true.
#true juga harus menggunakan huruf kapital di awal kata.
#True. Jika tidak error.

#--------------------------------------------------------------

#jika ingin menggunakan sort yang sementara, 
#atau dengan kata lain tidak mengubah urutan aslinya,
#pakai sorted()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Ini adalah urutan asli listnya {cars}")
print(f"\nIni adalah yang sudah di sort {sorted(cars)}")
print(f"\nIni adalah list aslinya lagi {cars}\n")

print(sorted(cars, reverse=True))
#di atas contoh sorted pakai reverse true.

#---------------------------------------------------------------

#jika ingin membalik urutan awal yang belum di sorted dll,
#bisa pakai cara di bawah ini.

print(cars)
cars.reverse()
print(cars)

#setelah pakai cara di atas urutan dalam list akan berubah
#secara permanen. kalau mau balikin tinggal reverse lagi aja.

#Jika ingin mengetahui panjang sebuah list, pakai
#len(). Di bawah ini contohnya

print(len(cars))

#hasilnya 4 sesuai dengan total item di dalam list.