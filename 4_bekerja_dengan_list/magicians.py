#jika ingin melakukan tindakan yang sama pada setiap item di
#dalam sebuah list pakai perulangan.

#di bawah ini salah satu contoh perulangan.
#perulangan for

magicians = ['Jovan', 'Deddy', 'Wowok']
#memasukkan item pertama ke dalam variabel magician
#kemudian lanjut ke baris kode berikutnya dan
#kembali ke sini lagi jika list masih ada item lain, dan 
#memasukkannya ke variabel kemudian melakukan hal yang sama
#hingga item habis akan lanjut ke baris kode di luar for.
#jika tidak ada maka berhenti.
for magician in magicians:
	#mencetak nilai dari variabel magician, yang berubah
	#setiap di print, hingga sudah tidak ada item di list
	print(magician)


#nama variabel setelah for kalau bisa harus jelas dan bermakna
#harus mewakili setiap item di list juga!
#misal list = books maka varnya book.

for magician in magicians:
	print(f"{magician}, itu adalah trik yang hebat! ")
	print(f"Saya tidak sabar melihat trik mu yang lain, {magician.title()}.\n")

#hasilnya nama magician selalu berganti
#menyesuaikan dengan item di dalam list magicians.
#baris di dalam for bisa ditambah lebih banyak jika kamu mau
#tidak ada batasan program di dalam perulangan for. contoh :

numbers = [1, 2, 3]

for number in numbers:
	print(number + 1)
	print(number + 10)
	print(number + 100)
	#dan seterusnya
	#jalankan untuk lihat hasilnya!

print("Terima kasih, semuanya. Itu adalah trik sulap yang luar biasa")
#jadi yang mengalami perulangan adalah yang ada di dalam for
#dapat dilihat dari adanya spasi atau tab di awal kalimat