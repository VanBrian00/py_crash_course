# Latihan 9 bab 8
def print_pesan(kumpulan_pesan):
	"""Fungsi untuk print pesan"""
	for pesan in kumpulan_pesan:
		print(pesan)

kumpulan_pesan_singkat = ["Hallo", "Hi", "Apa Kabar", "Pagi"]

print_pesan(kumpulan_pesan_singkat)

# Latihan 10 bab 8

print("")
sent_messages = []

def send_messages(kumpulan_pesan, sent_messages):
	"""Fungsi untuk kirim pesan"""
	for pesan in kumpulan_pesan[:]:
		sent_messages.append(pesan)
		print(pesan)
		kumpulan_pesan.remove(pesan)

send_messages(kumpulan_pesan_singkat, sent_messages)
print("")
print(kumpulan_pesan_singkat)
print(sent_messages)

# Latihan 11 bab 8

print("")
list_pesan2 = sent_messages
sent_messages = []

send_messages(list_pesan2[:], sent_messages)

print(f"ini adalah isi dari sent_messages {sent_messages}")
print(f"Ini adalah isi dari list_pesan2 {list_pesan2}")