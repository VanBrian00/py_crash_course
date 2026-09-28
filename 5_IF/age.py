age_0 = 22
age_1 = 18

#contoh penggunaan and pada if statement
#pakai dalam kurung agar lebih rapi dan mudah dibaca
if (age_0 >= 21) and (age_1 >= 21):
    print("Keduanya sudah cukup umur")
else:
    print("Salah satu dari mereka blm cukup umur")
    
if (age_0 >= 21) or (age_1 >= 21):
    print("Ya, salah satunya sudah cukup umur.\n")
else:
    print("Dua duanya blm cukup umur.\n")
    
age_1 = 22

if (age_0 >= 21) and (age_1 >= 21):
    print("Keduanya sudah cukup umur")
else:
    print("Salah satu dari mereka blm cukup umur")
    
age_0 = 18
age_1 = 18

if (age_0 >= 21) or (age_1 >= 21):
    print("Ya, salah satunya sudah cukup umur.\n")
else:
    print("Dua duanya blm cukup umur.\n")