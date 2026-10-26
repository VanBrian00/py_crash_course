# Jawaban latihan 8.6
def city_country(city, country):
	"""Mengembalikan nama kota berserta negaranya"""
	hasil = f"{city}, {country}"
	return hasil.title()

print(city_country('jakarta', 'indonesia'))
print(city_country('beijing', 'cina'))
print(city_country('tokyo', 'japan'))

# Jawaban latihan 8.7 
daftar_album = {}

print("")
def make_album(title='', artist='', jumlah_lagu=None):
	"""Album"""
	i = f"Album {len(daftar_album) + 1}"
	if title != '' and artist != '':
		if jumlah_lagu is not None:
			daftar_album[i] = {
				'Judul': title.title(),
				'artis': artist.title(),
				'total-lagu': f"{jumlah_lagu} lagu",
			}	
		else:
			daftar_album[i] = {
				'Judul': title.title(),
				'artis': artist.title(),
			}
			
		return daftar_album[i]

print(make_album('Covers Collection Vol.18', 'Shania Yan', '52'))
print(make_album('Open a Door', 'Aimer', '12'))
print(make_album('By Your Grace Live', 'ICI Worship', '9'))
print(make_album('A', 'Z'))

print()

# for a, b in daftar_album.items():
# 	print(f"{a}\n\t{b}\n")

# Jawaban latihan 8.8
while True:
	print("Ketik q dan enter jika tidak ingin lanjut memberikan input!")
	judul = input("Masukkan judul Album: ")
	if judul == 'q':
		break
	artist = input("Masukkan nama artisnya: ")
	if artist == 'q':
		break
	total_lagu = input("Masukkan jumlah lagu yang ada di Album:")
	if total_lagu == 'q':
		break

	make_album(judul, artist, total_lagu)

for a, b in daftar_album.items():
	print(f"{a}\n\t{b}\n")