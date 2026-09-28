adek_pertama = {
    'nama_depan' : 'Vincent',
    'nama_tengah' : 'Jovianto',
    'nama_belakang' : 'Gunawan',
    'umur' : 22,
    'kota' : 'Jakarta'
}

adek_kedua = {
    'nama_depan' : 'Johnsen',
    'nama_tengah' : 'Deandru',
    'nama_belakang' : 'Limanto',
    'umur' : 21,
    'kota' : 'Jakarta'
}
adek_ketiga = {
    'nama_depan' : 'Inggrid',
    'nama_tengah' : 'sharleen',
    'nama_belakang' : 'Gunawan',
    'umur' : 19,
    'kota' : 'Jakarta'
}

people = [adek_pertama, adek_kedua, adek_ketiga]

for adek in people:
    nama_lengkap = f"{adek['nama_depan']} {adek['nama_tengah']} {adek['nama_belakang']}"
    umur = adek['umur']
    kota = adek['kota']
    print(f"{nama_lengkap} berumur {umur} tahun dan tinggal di {kota}.")
    
anjing = {
    'jenis' : 'anjing',
    'nama' : 'Gabby',
    'ras' : 'Golden Retriever',
    'umur' : 5,
    'warna' : 'Cokelat',
    'pemilik' : 'Abel'
}

kucing = {
    'jenis' : 'kucing',
    'nama' : 'Bonny',
    'ras' : 'Persia',
    'umur' : 2,
    'warna' : 'putih',
    'pemilik' : 'Vincent'
}

burung = {
    'jenis' : 'burung',
    'nama' : 'Coco',
    'ras' : 'Parrot',
    'umur' : 2,
    'warna' : 'hijau',
    'pemilik' : 'Ryan'
}

hewan_peliharaan = [anjing, kucing, burung]

print("\b")
for hewan in hewan_peliharaan:
    print(f"{hewan['jenis'].title()} milik {hewan['pemilik']} bernama {hewan['nama']}, rasnya {hewan['ras']} dia"
        f" berumur {hewan['umur']} tahun dan berwarna {hewan['warna']}")
    
favorite_places = {
    'Jovan' : ['Paris', 'Tokyo'], 
    'Gaga' : ['New York', 'Malaysia'], 
    'Doragon' : ['London', 'Indonesia', 'Australia']
    }

for nama, tempat in favorite_places.items():
    if len(tempat) == 1 :
        print(f"\n {nama.title()} tempat favoritnya adalah {tempat[0]}.")
    else: 
        print(f"\n {nama.title()} tempat favoritnya adalah:")
        for t in tempat:
            print(f"\t- {t}")
            
angka_favorit_teman = {
    'Abel' : [2, 7],
    'Vincent' : 1,
    'Ryan' : [9, 5],
    'Gamma' : [3, 8],
    'Fendy' : 6
    }

for nama, angka in angka_favorit_teman.items():
    if isinstance(angka, int):
        print(f"\n{nama.title()} angka favoritnya adalah {angka}.")
    else:
        print(f"\n{nama.title()} angka favoritnya adalah:")
        for a in angka:
            print(f"\t- {a}")

cities = {
    'jakarta' : {
        'negara' : 'indonesia',
        'populasi' : 10_770_000,
        'fakta' : 'Jakarta adalah ibu kota Indonesia.'
    },
    'moskow' : {
        'negara' : 'rusia',
        'populasi' : 12_678_000,
        'fakta' : 'Moskow adalah ibu kota Rusia.'
    },
    'kuala lumpur' : {
        'negara' : 'malaysia',
        'populasi' : 1_780_000,
        'fakta' : 'Kuala Lumpur adalah ibu kota Malaysia.'
    },
}

for kota, info in cities.items():
    negara = info['negara']
    populasi = info['populasi']
    fakta = info['fakta']
    
    print(f"\nKota {kota.title()} berada di negara {negara.title()} dengan populasi sekitar {populasi} jiwa. "
          f"fakta menarik tentang kota ini yaitu {fakta}")
    
    
cities["London"] = {
    'negara' : 'inggris',
    'populasi' : 8_982_000,
    'fakta' : 'London adalah ibu kota Inggris.'
}

for kota, info in cities.items():
    kota = kota.title()
    negara = info['negara'].title()
    populasi = info['populasi']
    fakta = info['fakta']
    
    print(f"\nKota {kota} berada di negara {negara}.\n\t- Jumlah populasi = +-{populasi:,} jiwa."
          f"\n\t- Fakta menarik tentang kota ini = {fakta}")