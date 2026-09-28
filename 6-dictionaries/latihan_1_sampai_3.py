adek_pertama = {
    'nama_depan' : 'Johnsen',
    'nama_tengah' : 'Deandru',
    'nama_belakang' : 'Limanto',
    'umur' : 21,
    'kota' : 'Jakarta'
    }

print(adek_pertama)

angka_favorit_teman = {
    'Abel' : 2,
    'Vincent' : 1,
    'Ryan' : 5,
    'Gamma' : 8,
    'Fendy' : 6
    }

print(angka_favorit_teman)

glosari_python = {
    'looping' : 'proses mengulang suatu blok kode sampai kondisi tertentu terpenuhi',
    'list' : 'tempat menyimpan beberapa item/ data dalam satu variabel',
    'variabel' : 'tempat menyimpan suatu nilai',
    'dictionary' : 'tempat menyimpan beberapa key dan value yang berpasangan',
    'integer' : 'tipe data untuk bilangan bulat',
    }

for nama, pengertian in glosari_python.items():
    print(f"{nama} adalah {pengertian}.")