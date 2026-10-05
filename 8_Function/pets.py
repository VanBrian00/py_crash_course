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