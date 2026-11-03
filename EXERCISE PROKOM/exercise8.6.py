def city_country(city, country):
    """Kembalikan string berformat 'Kota, Negara'."""
    return f"{city.title()}, {country.title()}"

print(city_country('santiago', 'chile'))
print(city_country('jakarta', 'indonesia'))
print(city_country('canberra', 'australia'))