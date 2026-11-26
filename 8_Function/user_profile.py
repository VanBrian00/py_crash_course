# ** pada parameter dipakai untuk menerima argumen keyword tanpa batas.
# parameter user_info menjadi dictionary setelah diberi **
def build_profile(first, last, **user_info):
	"""membuat dictionary yang berisi semua yang kita tahu tentang user."""
	user_info['first_name'] = first
	user_info['last_name'] = last

	return user_info


user_profile = build_profile('Baba', 'Putin', Location='Australia', field='phusics')

print(user_profile)