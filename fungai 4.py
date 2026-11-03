# pi = 3.45
def volTabung(jariJari, tinggi):
    global pi
    pi = 3.14
    volume = pi * (jariJari ** 2) * tinggi
    return volume


print(pi)
volTab = volTabung(7, 10)
print(volTab)