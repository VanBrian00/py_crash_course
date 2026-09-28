Users = {
    'Dragon Slayer': {
        'first': 'John',
        'last': 'Lake',
        'location': 'Brazil',
    },
    'Wise Chazer': {
        'first': 'Jovan',
        'last': 'Febrian',
        'location': 'Indonesia',
    },
}

for username, user_info in Users.items():
    print(f"\nUsername: {username}")
    
    nama_lengkap = f"{user_info['first']} {user_info['last']}"
    lokasi = user_info['location']
    
    print(f"\tNama Lengkap: {nama_lengkap.title()}")
    print(f"\tLokasi: {lokasi.title()}")