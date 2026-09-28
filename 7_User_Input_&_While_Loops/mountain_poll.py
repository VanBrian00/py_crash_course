users_input = {}

flag = True

while flag:
	name = input("\nSiapa nama mu? ")
	response = input("Gunung mana yang ingin kamu panjat suatu hari? ")

	# simpan jawaban
	users_input[name] = response

	# Cari tahu apakah ada lagi yang mau ikut poling?
	ulangin = input(f"Apakah ada orang lain yang mau ikut poling? (yes/no) ")
	if ulangin == 'no':
		flag = False
		# poling berakhir

# Tampilkan hasil poling

print(f"\n--- Poll Results ---\n")

for name, response in users_input.items():
	print(f"{name} whould like to climb {response}.")
