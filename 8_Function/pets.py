def describe_pet(animal_type, pet_name):
    """Menampilkan Informasi Tentang Hewan Peliharaan"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet("cat", "nyon nyon")
describe_pet("dog", "Bambang")

# menggunakan argumen keyword, bedakan sendiri dengan yang di atas!
describe_pet(pet_name="gong",animal_type="bird")

# parameter yang memiliki nilai default harus di belakang!
def describe_pet(pet_name, animal_type="dog"):
    """Menampilkan Informasi Tentang Hewan Peliharaan"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name="Fuji")
describe_pet("toyo")
describe_pet("suzu","cat")

# hasil dari kode di bawah ini error karena butuh argumen buat isi parameter pet name.
# parameter animal_type sudah ada argumen default jadi gpp.
# describe_pet()

# di bawah ini juga bakal error
# describe_pet("toyo", "Pig", "Black")
# fungsinya hanya punya dua parameter, jadi 3 argumen gak bisa diberikan!