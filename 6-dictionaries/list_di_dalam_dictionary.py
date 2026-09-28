# simpan informasi tentang orderan pizza

pizza_orderan = {
    'roti': 'tipis',
    'topping': ['keju', 'sosis', 'jamur'],
}

# print informasi tentang orderan pizza
print(f"Pizza yang kamu pesan menggunakan roti {pizza_orderan['roti']}, dengan"
      "topping berikut:")

n = 1
for topping in pizza_orderan['topping']:
    print(f"\t{n}. {topping}")
    n += 1
    
    
bahasa_pemograman_favorit = {
    'Zen': ['python', 'java'],
    'Jovan': ['python', 'php'],
    'Kai': ['c++', 'C#'],
    'Pai': ['golang'],
    'Dot': ['Java', 'c++'],
}

for nama, bahasa in bahasa_pemograman_favorit.items():
    if len(bahasa) > 1:
        n = 1
        print(f"\n{nama} menyukai bahasa pemograman berikut:")
        for b in bahasa:
            if b.lower() == 'php':
                print(f"\t{n}. {b.upper()}")
                n += 1
            else:
                print(f"\t{n}. {b.title()}")
                n += 1
    elif len(bahasa) == 1:
        bahasa = bahasa[0];
        if bahasa.lower() == 'php':
            print(f"\n{nama} menyukai bahasa pemograman {bahasa.upper()}")
        else:
            print(f"\n{nama} menyukai bahasa pemograman {bahasa.title()}")