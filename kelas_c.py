tinggi_badan= [170, 165, 180, 175, 160]
print("tinggi badan mahasiswa:", tinggi_badan [0])
print("Jumlah mahasiswa: ", len (tinggi_badan))
tinggi_badan.append(185)
#penambahan data tinggi mahasiswa baru sebanyak 40 dengan loop 
import random as rn
for i in range(40):
    tinggi_badan.append (int(rn.uniform(150, 200)))

print(len(tinggi_badan)) 
print(tinggi_badan)