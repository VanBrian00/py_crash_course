# alien_satu = {
#     'color': 'green',
#     'points': 5,
# }
# alien_dua = {
#     'color': 'green',
#     'points': 5,
# }
# alien_tiga = {
#     'color': 'green',
#     'points': 5,
# }

# semua_alien = [alien_satu, alien_dua, alien_tiga]

# for alien in semua_alien:
#     print(alien)

aliens = []

# buat 30 alien pakai for loop
for alien_number in range(30):
    alien = {
        'color': 'green',
        'speed': 'slow',
        'points': 5,      
    }
    aliens.append(alien)
    
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
for alien in aliens[:5]:
    print(alien)
    
print(f"\nJumlah alien: {len(aliens)}")