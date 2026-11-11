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