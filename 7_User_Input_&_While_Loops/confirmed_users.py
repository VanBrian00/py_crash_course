# daftar orang yang belum verifikasi
unconfirmed_users = ['gugu', 'zaza', 'baba']
# daftar orang yang sudah
confirmed_users = []

# perulangan while
while unconfirmed_users:
	# user sekarang, diambil dari user yang belum di verifikasi dari belakang dan di hapus dari list yang belum
	currend_user = unconfirmed_users.pop()
	# print
	print(f"Verifying user: {currend_user.title()}")
	# masukkin yang sudah di verifikasi dengan append
	confirmed_users.append(currend_user)

print("\nThe following users have been confirmed:")
for u in confirmed_users:
	print(u.title())