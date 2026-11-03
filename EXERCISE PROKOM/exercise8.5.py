def describe_city(city, country='indonesia'):
    """Cetak kalimat sederhana tentang kota dan negaranya."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('surabaya')
describe_city('denpasar')
describe_city('reykjavik', 'iceland')
