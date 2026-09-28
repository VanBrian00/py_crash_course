# Jawaban untuk soal 7.8 dan 7.9
sandwich_orders = ['Club Sandwich', 'Pastrami', 'Submarine Sandwich', 'Pastrami', 'Banh Mi', 'Cuban sandwich', 'Fruit Sando', 'Pastrami']
finished_sandwiches = []

print("Maaf, sandwich pastrami sudah habis.\n")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"{current_sandwich} telah selesai dibuat.")
    finished_sandwiches.append(current_sandwich)
    
print("\n--- Sandwich yang Sudah Jadi ---")
for sandwich in finished_sandwiches:
    print(f"\t- {sandwich}")
    
# Jawaban untuk soal 7.10

polling_results = {}
flag = True

while flag:
    nama = input("\nSiapa nama mu ")
    tempat_liburan = input("Jika kamu bisa mengunjungi satu tempat di dunia, ke mana kamu akan "
                           "pergi? ")
    
    polling_results[nama] = tempat_liburan
    
    lanjut = input("Apakah ada orang lain yang ingin ikut polling? (yes/no) ")
    
    if lanjut.lower() == 'no':
        flag = False
        
print("\n--- Hasil Polling ---")
for nama, tempat_liburan in polling_results.items():
    print(f"{nama} ingin pergi ke {tempat_liburan}.")