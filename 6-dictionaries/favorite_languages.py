bahasa_pemograman_favorit = {
    'Agus': 'python',
    'Budi': 'C++',
    'Hana': 'PHP',
    'Dewi': 'Java',
    }

for nama, bahasa_favorit in bahasa_pemograman_favorit.items():
    if bahasa_favorit != 'PHP':
        print(f"Bahasa pemograman favorit {nama.title()} adalah {bahasa_favorit.title()}")
    else:
        print(f"Bahasa pemograman favorit {nama.title()} adalah {bahasa_favorit.upper()}")
        
for name in bahasa_pemograman_favorit:
    print(name.title())
    
teman = ['Dewi', 'Budi']

for nama in bahasa_pemograman_favorit.keys():
    print(f"Hi {nama.title()}.")
    
    if nama in teman:
        bahasa = bahasa_pemograman_favorit[nama].title()
        print(f"\t{nama.title()}, saya melihat kamu saka bahasa {bahasa}!")
        
if 'erin' not in bahasa_pemograman_favorit.keys():
    print("Erin, tolong ikuti survei!")
    
for nama in sorted(bahasa_pemograman_favorit.keys()):
    print(f"{nama.title()}, terima kasih sudah mengikuti survei!")
    
for bahasa in bahasa_pemograman_favorit.values():
    if bahasa.lower() == 'php' :
        print(bahasa.upper())
    else:
      print(bahasa.title())
      
# Pakai Set agar datanya unik/ tidak ada yang duplikat
bahasa_pemograman_favorit['Jovan'] = 'python'
print(bahasa_pemograman_favorit)

for bahasa in set(bahasa_pemograman_favorit.values()):
    if bahasa.lower() == 'php' :
        print(bahasa.upper())
    else:
      print(bahasa.title())