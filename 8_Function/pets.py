def describe_pet(animal_type, pet_name):
    """Menampilkan Informasi Tentang Hewan Peliharaan"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet("cat", "nyon nyon")
describe_pet("dog", "Bambang")