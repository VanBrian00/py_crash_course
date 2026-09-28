teks = "\nBeri tahu saya sesuatu, dan saya akan memberi tahu balik ke kamu! "
teks += "\nMasukkan 'quit' untuk mengakhiri program. "

status = True

while status:
	message = input(teks)
	if message != 'quit':
		print(message)
	else:
		status = False