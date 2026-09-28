#cek apakah isi pesanan adalah pepperoni?
#jika bukan maka print ini bukan pepperoni.

topping_pesanan = 'jamur'

if topping_pesanan != 'pepperoni':
    print("Ini bukan pepperoni.")
    
#memeriksa apakah sebuah item ada di dalam list 
#dengan menggunakan operator in

topping_yang_diminta = ['jamur', 'bawang', 'nanas']

print('jamur' in topping_yang_diminta)
print('pepperoni' in topping_yang_diminta)

#in digunakan untuk memberi tahu komputer untuk
#memeriksa apakah ada jamur dan pepperoni di dalam list.

topping_pesanan = ['jamur', 'ekstra keju']

if 'jamur' in topping_pesanan:
    print("\nmenambahkan jamur.")
if 'pepperoni' in topping_pesanan:
    print("\nmenambahkan pepperoni.")
if 'ekstra keju' in topping_pesanan:
    print("\nmenambahkan ekstra keju.")
    
print(f"\nPesananan anda sudah selesai.")

topping_pesanan = ['jamur', 'paprika hijau', 'ekstra keju']

for topping in topping_pesanan:
    if topping == 'paprika hijau':
        print(f"\nMohon maaf, kamu kehabisan {topping}.")
    else:
        print(f"\nmenambahkan {topping}.")
    
print("\nPizza pesanan anda sudah selesai di buat.")

topping_pesanan = []

if topping_pesanan:
    for topping in topping_pesanan:
        print(f"\nmenambahkan {topping}.")
    print("\npizza pesanan anda sudah selesai di buat.")
else: 
    print(f"\nAnda yakin mau pizza polos?")
    
topping_yang_tersedia = ['jamur', 'zaitun', 'paprika hijau', 'pepperoni', 'nanas', 'ekstra keju']

topping_pesanan = ['jamur', 'kentang goreng', 'ekstra keju']

for topping in topping_pesanan:
    if topping in topping_yang_tersedia:
        print(f"\nmenambahkan {topping}.")
    else:
        print(f"\nMaaf, kami tidak memiliki {topping}.")
        
print("\nPizza pesanan anda sudah selesai di buat.")