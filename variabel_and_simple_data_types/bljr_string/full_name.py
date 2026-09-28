nama_awal = "ada"
nama_belakang = "lovelace"
nama_lengkap = f"{nama_awal} {nama_belakang}"
print(nama_lengkap)

#contoh di atas disebut f-strings.
#f berarti format.
#gunakan tanda kurung kurawal {} dan isi dengan nama variabel
#jika ingin mengambil nilai dari sebuah variabel!

print(f"Hallo {nama_lengkap.title()}. Apakah kamu sehat?")

pesan = f"{nama_lengkap.title()} jangan lupa belajar!"
print(pesan)

#jika pakai versi <= 3.5 maka cara pakainya berbeda.
#jadi nama_lengkap = "{} {}".format(nama_awal, nama_belakang)
#dalam pemrograman, whitespace adalah karakter 
#yang tidak akan dicetak, seperti spasi, tab 
#dan simbol di akhir baris
#whitespace ini dapat dipakai agar output mudah dibaca

print("\ttab")

#gunakan \t untuk menambahkan tab pada output.
#hasilnya nanti : "		tab"

print("jenis-jenis kendaraan :\n1. roda empat\n2. roda dua")

#gunakan \n untuk bikin baris baru, 
#jadi nanti setelah \n akan berada di baris baru
#\n dan \t dapat digunakan secara bersamaan.
#kita bisa pakai rstrip() untuk menghilangkan spasi di kanan
#untuk kiri pakai lstrip()
#untuk dua sisi bisa pakai strip()

mobil = " toyota "
print(mobil)
print(mobil.rstrip())
print(mobil.lstrip())
print(mobil.strip())

#cara di atas tidak permanen
#jika ingin permanen masukkan ulang ke variabel tersebut

mobil = mobil.strip()
print(f"ini tanpa spasi dan permanen :{mobil}.")