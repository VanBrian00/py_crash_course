tujuan_wisata = ['Jepang', 'Korea', 'China', 'Saturnus', 'Mars']
#print
print(tujuan_wisata)
#sort sesuai alfabet dan print
print(sorted(tujuan_wisata))
print(tujuan_wisata)
#sort sesuai alfabet tapi dari belakang dan print
print(sorted(tujuan_wisata, reverse=True))
print(tujuan_wisata)
#Balikkin urutan list secara permanent
tujuan_wisata.reverse()
print(tujuan_wisata)
tujuan_wisata.reverse()
print(tujuan_wisata)
#sort juga tapi ini permanent
tujuan_wisata.sort()
print(tujuan_wisata)
tujuan_wisata.sort(reverse = True)
print(tujuan_wisata)

#print jumlah item di dalam list
print(f"\nJumlah lokasi tujuan wisata {len(tujuan_wisata)}\n")

#list gunung
gunung = ['Merbabu', 'Merapi', 'Krakatau', 'Miyoboki', 'Sinai']
#print semua gunung
print(gunung)
#print gunung Krakatau
print(gunung[2])
#print gunung Merbabu dengan format title, karena huruf depan
#sudah huruf kapital jadi tidak ada yang berubah
print(gunung[0].title())
#print yang paling belakang, yaitu gunung Sinai
print(gunung[-1])
#masukkan Gunung kerinci di posisi ke empat
gunung.insert(3, 'Kerinci')
#tambahin gunung fuji di belakang 
gunung.append('Fuji')
print(gunung)
#hapus gunung yang ada di akhir list
gunung.pop()
print(gunung)