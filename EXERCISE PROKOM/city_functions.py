"""A collection of functions for working with cities.""" 

def city_country(city, country, population=''): 
    """Return a string representing a city-country pair. 
    
    Returns a string like 'Santiago, Chile', or, when a population is 
    given, 'Santiago, Chile – population 5000000'. 
    """ 
    
    output_string = f"{city.title()}, {country.title()}" 
    if population: 
        output_string += f" – population {population}" 
    return output_string