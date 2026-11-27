# Latihan 12 bab 8

def isi_sandwich(*kumpulan_isi):
	"""Fungsi untuk menerima dan menampilkan isi sandwich"""
	print("sandwich yang dipesan berisi:")
	for isi in kumpulan_isi:
		print(f"- {isi}")

isi_sandwich('Telur', 'tomat')
isi_sandwich('Daging', 'Mie')
isi_sandwich('Sosis', 'Cabe', 'Tomat', 'Keju')