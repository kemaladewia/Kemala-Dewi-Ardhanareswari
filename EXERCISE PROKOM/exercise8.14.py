def make_car(manufacturer, model, **car_info):
    """Buat dictionary yang mewakili sebuah mobil."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car = make_car('toyota', 'avanza', color='silver', seats=7)
print(car)