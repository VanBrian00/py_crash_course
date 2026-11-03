def print_models(uprinted_designs, completed_models):
	""" Fungsi untuk print model desain """
	# perulangan untuk memindahkan yang sudah di print,
	# sampai tidak ada lagi desain yang perlu di print.
	while uprinted_designs:
		current_design = uprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	""" Fungsi untuk menampilkan print models yang telah selesai """
	# Menampilkan semua models yang sudah selesai di print.
	# Menggunakan perulangan for.
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model)

# list yang berisi disain yang belum di print.
uprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']

# list untuk menampung model desain yang sudah selesai.
completed_models = []

print_models(uprinted_designs, completed_models)
show_completed_models(uprinted_designs)
show_completed_models(completed_models)