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