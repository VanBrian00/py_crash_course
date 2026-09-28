# merk_mobil = input("Mobil apa yang kamu cari? ")
# print(f"Oke, saya akan berusaha mencari mobil {merk_mobil} yang sesuai dengan anda.")

# tamu_resto = int(input("Berapa orang yang datang ke restoran? "))

# if tamu_resto > 8:
#     print("Maaf, anda harus menunggu karena restoran sedang penuh.")
# else:
#     print("Silahkan masuk, meja tersedia untuk anda.")

angka_kelipatan_10 = float(input("Tolong berikan saya angka dan saya akan menilai apakah dia kelipatan dari 10! "))
perhitungan = angka_kelipatan_10 % 10

if perhitungan == 0 :
    print(f"Angka {angka_kelipatan_10} adalah kelipatan dari 10.")
else:
    print(f"Angka {angka_kelipatan_10} bukan kelipatan 10.")