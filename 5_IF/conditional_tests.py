buah = "Apel"

print("Jovan memprediksi bahwa itu adalah Semangka")
print(buah == "Apel")
print("\nJovan memprediksi bahwa itu adalah Apel")
print(buah == "Apel")

daftar_nama = ["Jokowi", "Prabowo", "Sandiaga"]

print("\napakah nama 'Jokowi' ada di dalam daftar_nama?")
print("Jokowi" in daftar_nama)
print("\n'Ahok' tidak ada di dalam daftar_nama?")
print("Ahok" not in daftar_nama)

if ("Jokowi" in daftar_nama) and ("Ahok" in daftar_nama):
    print("\nJokowi dan Ahok ada di dalam daftar_nama")
else:
    print("\nJokowi dan Ahok tidak ada di dalam daftar_nama")

if (buah == "Apel") or (buah == "Pisang"):
    print("\nSaya akan makan buah itu")
else:
    print("\nSaya tidak akan makan buah itu")
    
print("apel" == buah.lower())

x = 14
if (x == 14) :
    print("\nNilai x sama dengan 14")
if (x != 14) :
    print("\nNilai x tidak sama dengan 14")
if (x > 14) :
    print("\nNilai x lebih besar dari 14")
if (x < 14) :
    print("\nNilai x lebih kecil dari 14")
if (x >= 14) :
    print("\nNilai x lebih besar atau sama dengan 14")
if (x <= 14) :
    print("\nNilai x lebih kecil atau sama dengan 14")