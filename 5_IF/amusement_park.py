age = 12

if age < 4:
    harga= "free"
elif age < 18:
    harga= "$25"
elif age < 65:
    harga= "$40"
elif age >= 65 and age < 100:
    harga= "$20"
    
print(f"Your admission cost is {harga}.")