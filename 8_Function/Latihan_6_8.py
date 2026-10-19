def city_country(city, country):
	"""Mengembalikan nama kota berserta negaranya"""
	hasil = f"{city}, {country}"
	return hasil.title()

print(city_country('jakarta', 'indonesia'))
print(city_country('beijing', 'cina'))
print(city_country('tokyo', 'japan'))