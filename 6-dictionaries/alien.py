# Buat dictionay
alien_0 = {'color': 'green', 'points': 5}

# print isi dictionary
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']

print(f"Kamu baru saja mendapatkan {new_points} poin!")

print(alien_0)

# tambahin key dan value baru ke dictionary
alien_0['x'] = 0
alien_0['y'] = 25

print(alien_0)

alien_1 = {}

alien_1['color'] = 'yellow'
alien_1['points'] = 10

print(alien_1)

alien_0['color'] = 'yellow'

print(f"Alien pertama sekarang berwarana {alien_0['color']}")

alien_0['speed'] = 'medium'

print(f"Posisi ori alien pertama: {alien_0['x']}")

# gerakkan alien ke kanan
# tentukan jarak yang akan ditempuh alien berdasarkan kecepatannya

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # hanya untuk alien cepat, kalau bisa lain kali pakai elif aja
    x_increment = 3
    
# posisi baru alien adalah posisi lama ditambah jarak yang ditempuh

alien_0['x'] = alien_0['x'] + x_increment

print(f"Posisi baru alien pertama: {alien_0['x']}")
    
del alien_0['points']
#key point hilang secara permanen berserta isinya/ nilainya

print(alien_0)

nilai_kecepatan = alien_1.get('speed', '')

print(nilai_kecepatan)