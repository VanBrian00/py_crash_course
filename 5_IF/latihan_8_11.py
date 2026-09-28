# user_names = ['admin', 'john', 'Lilis', 'Uranus', 'Venti']
user_names = []
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print(f"Hello {user_name}, would you like to see a status report?")
        else:
            print(f"Hello {user_name}, thank you for logging in again.")
else:
    print("We need to find some users!")
    
current_users = ['admin', 'john', 'Lilis', 'Uranus', 'Venti']
lower_current_users= []

for current_user in current_users:
    lower_current_users.append(current_user.lower())

new_users = ['Gugu', 'john', 'Saber', 'Uranus', 'Cinta']

for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print(f"Maaf, nama {new_user} sudah digunakan, silahkan gunakan nama lain.")
    else:
        print(f"Nama {new_user} tersedia.")
        
kumpulan_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for angka in kumpulan_angka:
    if angka == 1:
        print(f"{angka}st")
    elif angka == 2:
        print(f"{angka}nd")
    elif angka == 3:
        print(f"{angka}rd")
    else:
        print(f"{angka}th")