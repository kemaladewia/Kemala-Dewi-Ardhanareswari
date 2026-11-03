import matematika.geometry as geo

def main():
jari2 = float(input("Masukkan jari-jari lingkaran: "))
tinggi = float(input("Masukkan tinggi tabung: "))
volTab= geo.volTabung(geo.luasLingkaran(jari2), tinggi)

print("Volume Tabung ", volTab)

if __name__=="__main__":
    main()