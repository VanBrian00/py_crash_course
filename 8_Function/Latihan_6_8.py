def city_country(city, country):
	"""Mengembalikan nama kota berserta negaranya"""
	hasil = f"{city}, {country}"
	return hasil.title()

print(city_country('jakarta', 'indonesia'))
print(city_country('beijing', 'cina'))
print(city_country('tokyo', 'japan'))

daftar_album = {}

print("")
def make_album(title='', artist='', jumlah_lagu=1):
	"""Album"""
	i = f"Album {len(daftar_album) + 1}"
	if title != '' and artist != '':
		daftar_album[i] = {
			'Judul': title.title(),
			'artis': artist.title(),
			'total-lagu': f"{jumlah_lagu} lagu",
		}

make_album('Covers Collection Vol.18', 'Shania Yan', '52')
make_album('Open a Door', 'Aimer', '12')
make_album('By Your Grace Live', 'ICI Worship', '9')

for a, b in daftar_album.items():
	print(f"{a}\n\t{b}\n")