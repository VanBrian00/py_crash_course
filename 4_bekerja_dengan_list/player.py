players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#players[0:3] maksudnya adalah print item 1 sampai yang ke 3

print(players[1:4])
#jadi satu itu untuk item ke 2!

print(players[3:])
#di atas karena hanya 3 berarti yang di print adalah item ke 4
#tidak ada angka di belakang : artinya tidak ada batasan/ sampai item habis

print(players[:2])
#dia mulai dari awal dan berakhir di item ke 2

print(players[0::2])
#0 di awal sama seperti sebelumnya artinya mulai dari awal, bisa juga tidak diisi
#angka ke dua kosong artinya sampai habis
#angka ke 3, 2 artinya skip 1 item. 

print("\nini adalah 3 pemain saya dari urutan pertama!")
for players in players[:3]:
	print(players.title())