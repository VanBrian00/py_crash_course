glosari_python = {
    'looping' : 'proses mengulang suatu blok kode sampai kondisi tertentu terpenuhi',
    'list' : 'tempat menyimpan beberapa item/ data dalam satu variabel',
    'variabel' : 'tempat menyimpan suatu nilai',
    'dictionary' : 'tempat menyimpan beberapa key dan value yang berpasangan',
    'integer' : 'tipe data untuk bilangan bulat',
    'string' : 'tipe data untuk teks',
    'indetasi' : 'jarak spasi yang diberikan pada awal baris kode',
    'boolean' : 'tipe data untuk nilai benar atau salah',
    'if statement' : 'kondisi yang dipakai untuk membuat keputusan dalam program',
    'comment' : 'cacatan kecil yang ditulis di program dan tidak akan dieksekusi oleh komputer',
    }

for nama, pengertian in glosari_python.items():
    print(f"{nama} adalah {pengertian}.")
    
sungai_besar_di_indonesia = {
    "Kapuas" : "Kalimantan",
    "Batanghari" : "Sumatra Barat",
    "Musi" : "Sumatra Selatan",
}

for sungai, lokasi in sungai_besar_di_indonesia.items():
    print(f"Sungai {sungai} melintasi {lokasi}.")
    
for sungai in sungai_besar_di_indonesia.keys():
    print(f"{sungai}")
    
for lokasi in sungai_besar_di_indonesia.values():
    print(f"{lokasi}")

bahasa_pemograman_favorit = {
    'Agus': 'python',
    'Budi': 'C++',
    'Hana': 'PHP',
    'Dewi': 'Java',
    }

daftar_teman = ['Agus', 'Dewi', 'Budi', 'Hana', 'Erin', 'Saikoji', 'Bambang']

for teman in daftar_teman:
    if teman in bahasa_pemograman_favorit.keys():
        print(f"Terimakasih {teman} sudah mengikuti survei!")
    else:
        print(f"{teman}, tolong ikuti survei!")