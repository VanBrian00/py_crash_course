# * sebelum toppings itu untuk beri tahu kalau itu tupple.
# tupple pada parameter digunakan untuk menampung beberapa argumen.	
def make_pizza(*toppings):
	"""print list topping yang dipesan."""
	print("Daftar topping untuk pizza yang dipesan: ")
	for topping in toppings:
		print(f"- {topping}")

make_pizza("keju")
print("")
make_pizza("keju", "sosis", "sambel")


# Jika ada parameter lain
def make_pizza(size, *toppings):
	"""print list topping yang dipesan."""
	print(f"Daftar topping untuk pizza yang dipesan dengan ukuran {size} inci: ")
	for topping in toppings:
		print(f"- {topping}")

make_pizza(15,	"keju")
print("")
make_pizza(20 ,"keju", "sosis", "sambel")