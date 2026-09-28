#membuat list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

#untuk menampilkan seluruh isi list.
print(bicycles)

#jika ingin ambil salah satu data di dalam list,
#pakai cara di bawah ini.
#urutan awal list mulai dari angka 0.
#hasilnya nanti tanpa kurung siku, berbeda dari yang di atas.

print(bicycles[2])

#kita bisa beri metode seperti pada string.
#di bawah ini salah satu contohnya.

print(bicycles[0].title())

#jika ingin mengambil item paling belakang, 
#tapi tidak tahu itu nomor ke berapa,
#pakai -1 untuk mengambilnya
#contoh :

print(bicycles[-1])

#jika ingin ambil yang ke 2 dari belakang pakai -2
#begitu seterusnya.

#kita bisa ambil salah satu nilai dari list 
#dan dimasukkan ke variabel untuk dijadikan kalimat atau lainnya.
#contoh :

message = f"Sepeda pertama saya adalah {bicycles[0].title()}."
print(message)