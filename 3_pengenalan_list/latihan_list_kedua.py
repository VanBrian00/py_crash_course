daftar_tamu = ['Jokowi', 'Prabowo', 'Susilo']

print(f"{daftar_tamu[0]} selamat anda di undang ke pesta!")
print(f"{daftar_tamu[1]} selamat anda di undang ke pesta!")
print(f"{daftar_tamu[2]} selamat anda di undang ke pesta!")

tidak_bisa_hadir = daftar_tamu[1]

print(f"{tidak_bisa_hadir} tidak bisa datang!")
daftar_tamu[1] = 'Megawati'

print(f"{daftar_tamu[0]} selamat anda di undang ke pesta!")
print(f"{daftar_tamu[1]} selamat anda di undang ke pesta!")
print(f"{daftar_tamu[2]} selamat anda di undang ke pesta!")

print(f"{daftar_tamu[0]}, {daftar_tamu[1]}, dan {daftar_tamu[2]} saya menemukan meja makan yang lebih besar. Mari pindah!")

daftar_tamu.insert(0, 'Fufufafa')
daftar_tamu.insert(2, 'Gusdur')
daftar_tamu.append('Suharto')

print(f"{daftar_tamu[0]} selamat anda di undang ke pesta!")
print(f"{daftar_tamu[1]} selamat anda di undang ke pesta!")
print(f"{daftar_tamu[2]} selamat anda di undang ke pesta!")
print(f"{daftar_tamu[3]} selamat anda di undang ke pesta!")
print(f"{daftar_tamu[4]} selamat anda di undang ke pesta!")
print(f"{daftar_tamu[5]} selamat anda di undang ke pesta!")

print(f"maaf anda hanya dapat mengundang dua orang saja.")
print(f"{daftar_tamu.pop()} dikeluarkan dari pesta.")
print(f"{daftar_tamu.pop()} dikeluarkan dari pesta.")
print(f"{daftar_tamu.pop()} dikeluarkan dari pesta.")
print(f"{daftar_tamu.pop()} dikeluarkan dari pesta.")

print(f"Tamu yang tersisa adalah {daftar_tamu[0]}, dan {daftar_tamu[1]}")

del daftar_tamu[1]
del daftar_tamu[0]

print(daftar_tamu)