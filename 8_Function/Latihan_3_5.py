def make_shirt(size, text):
	"""Buat Baju"""
	print(f"Baju yang anda pesan ukuran {size}, dengan tulisan '{text}'")

# positional argument
make_shirt("L", "I Love U")
# keyword argument
make_shirt(text="U Cool", size="XL")

def make_shirt(size, text=""):
	"""Buat Baju"""
	size = size.lower()
	if size == "besar" or size == "xl":
		text = "I Love Python"
		print(f"Baju yang anda pesan ukuran {size}, dengan tulisan '{text}'")
	else:
		print(f"Baju yang anda pesan ukuran {size}, dengan tulisan '{text}'")

make_shirt("Besar")