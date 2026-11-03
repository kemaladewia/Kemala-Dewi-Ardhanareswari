# Soal 4 - Praktik fungsi/metode operasi pada List di Python

buah = ["apel", "jeruk", "mangga"]
print("List awal            :", buah)

# 1. append() - menambah satu elemen di akhir
buah.append("pisang")
print("append('pisang')     :", buah)

# 2. insert() - menyisipkan elemen di indeks tertentu
buah.insert(1, "anggur")
print("insert(1, 'anggur')  :", buah)

# 3. extend() - menambahkan banyak elemen dari list lain
buah.extend(["salak", "jeruk"])
print("extend([...])        :", buah)

# 4. len() - panjang list
print("len(buah)            :", len(buah))

# 5. Akses indeks & indeks negatif
print("buah[0]              :", buah[0])
print("buah[-1]             :", buah[-1])

# 6. Slicing
print("buah[1:4]            :", buah[1:4])
print("buah[::2]            :", buah[::2])

# 7. index() - mencari posisi elemen pertama
print("index('mangga')      :", buah.index("mangga"))

# 8. count() - menghitung kemunculan elemen
print("count('jeruk')       :", buah.count("jeruk"))

# 9. Operator in - cek keanggotaan
print("'salak' in buah      :", "salak" in buah)

# 10. Mengubah elemen
buah[0] = "apel malang"
print("buah[0] = ...        :", buah)

# 11. remove() - menghapus berdasarkan nilai (yang pertama ditemukan)
buah.remove("jeruk")
print("remove('jeruk')      :", buah)

# 12. pop() - menghapus berdasarkan indeks & mengembalikan nilainya
diambil = buah.pop()
print("pop()                :", buah, "-> diambil:", diambil)
diambil = buah.pop(1)
print("pop(1)               :", buah, "-> diambil:", diambil)

# 13. del - menghapus elemen/slice
del buah[0]
print("del buah[0]          :", buah)

# 14. sort() & sorted()
angka = [5, 2, 9, 1, 7]
print("\nList angka           :", angka)
print("sorted(angka)        :", sorted(angka), "(list asli tetap:", angka, ")")
angka.sort()
print("sort()               :", angka)
angka.sort(reverse=True)
print("sort(reverse=True)   :", angka)

# 15. reverse() - membalik urutan
angka.reverse()
print("reverse()            :", angka)

# 16. min(), max(), sum()
print("min / max / sum      :", min(angka), max(angka), sum(angka))

# 17. copy() - salinan, bukan referensi yang sama
salinan = angka.copy()
alias = angka
salinan.append(100)
print("copy() lalu append   : salinan =", salinan, "| asli =", angka)
alias.append(50)
print("alias = angka        : alias =", alias, "| asli ikut berubah =", angka)

# 18. Penggabungan (+) dan perkalian (*)
print("[1, 2] + [3, 4]      :", [1, 2] + [3, 4])
print("['ha'] * 3           :", ["ha"] * 3)

# 19. List comprehension
kuadrat = [x ** 2 for x in range(1, 6)]
genap = [x for x in range(1, 11) if x % 2 == 0]
print("\nKuadrat 1-5          :", kuadrat)
print("Genap 1-10           :", genap)

# 20. enumerate() dan zip()
for i, b in enumerate(["teh", "kopi"]):
    print(f"enumerate -> indeks {i}: {b}")
for nama, nilai in zip(["Ani", "Budi"], [85, 90]):
    print(f"zip -> {nama}: {nilai}")

# 21. Nested list (list 2 dimensi)
matriks = [[1, 2, 3], [4, 5, 6]]
print("\nmatriks[1][2]        :", matriks[1][2])

# 22. clear() - mengosongkan list
angka.clear()
print("clear()              :", angka)