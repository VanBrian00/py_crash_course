def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""

	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('Jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=""):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"

	return full_name.title()

people_name = get_formatted_name('Kiki', 'Baz')
print(people_name)
people_name = get_formatted_name('Jovan', 'Limanto', 'Febrian')
print(people_name)