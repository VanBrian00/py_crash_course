def greet_users(names):
	"""Print sapaan simpel untuk setiap user di dalam list."""
	for name in names:
		pesan = f"Hello, {name.title()}!"
		print(pesan)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)