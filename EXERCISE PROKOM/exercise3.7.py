Guest_List = ['Nabila', 'Aira', 'Rara', 'Ulfi', 'Puyes']
print(f"Hello {Guest_List[0]}, ayo datang ke acara dinner di rumahku!")
print(f"Hello {Guest_List[1]}, ayo datang ke acara dinner di rumahku!") 
print(f"Hello {Guest_List[2]}, ayo datang ke acara dinner di rumahku!")
print(f"Hello {Guest_List[3]}, ayo datang ke acara dinner di rumahku!")
print(f"Hello {Guest_List[4]}, ayo datang ke acara dinner di rumahku!")

# Nabila tidak bisa datang ke acara dinner
tidak_bisa_datang = Guest_List[0]
print(f"\nSayangnya {tidak_bisa_datang} tidak bisa datang")

# Menambahkan tamu baru
tamu_baru = 'Vela'
Guest_List[0] = tamu_baru

print(f"Hello {Guest_List[0]}, ayo datang ke acara dinner di rumahku!")
print(f"Hello {Guest_List[1]}, ayo datang ke acara dinner di rumahku!") 
print(f"Hello {Guest_List[2]}, ayo datang ke acara dinner di rumahku!")
print(f"Hello {Guest_List[3]}, ayo datang ke acara dinner di rumahku!")
print(f"Hello {Guest_List[4]}, ayo datang ke acara dinner di rumahku!")

print("\nAda kabar baik! Aku mendapatkan meja yang jauh lebih besar, jadi aku akan mengundang lebih banyak tamu")

Guest_List.insert(0, 'Salsa')
Guest_List.insert(2, 'Nayya')
Guest_List.insert(3, 'Keira')
Guest_List.append('Zahra')

print(f"Hello {Guest_List[0]}, ayo datang ke acara dinner di rumahku!")
print(f"Hello {Guest_List[1]}, ayo datang ke acara dinner di rumahku!") 
print(f"Hello {Guest_List[2]}, ayo datang ke acara dinner di rumahku!")
print(f"Hello {Guest_List[3]}, ayo datang ke acara dinner di rumahku!")
print(f"Hello {Guest_List[4]}, ayo datang ke acara dinner di rumahku!")
print(f"Hello {Guest_List[5]}, ayo datang ke acara dinner di rumahku!")
print(f"Hello {Guest_List[6]}, ayo datang ke acara dinner di rumahku!") 
print(f"Hello {Guest_List[7]}, ayo datang ke acara dinner di rumahku!")
print(f"Hello {Guest_List[8]}, ayo datang ke acara dinner di rumahku!")

print("\nAku baru saja dapat kabar buruk, bahwa meja yang kupesan terlambat dikirim, sehingga aku hanya bisa mengundang dua orang saja.")

removed_guest0 = Guest_List.pop()
print(f"\nMaaf {removed_guest0}, maaf aku tidak jadi mengundangmu ke acara dinner di rumahku.")
removed_guest1 = Guest_List.pop()
print(f"\nMaaf {removed_guest1}, maaf aku tidak jadi mengundangmu ke acara dinner di rumahku.")
removed_guest2 = Guest_List.pop()
print(f"\nMaaf {removed_guest2}, maaf aku tidak jadi mengundangmu ke acara dinner di rumahku.")
removed_guest3 = Guest_List.pop()       
print(f"\nMaaf {removed_guest3}, maaf aku tidak jadi mengundangmu ke acara dinner di rumahku.")
removed_guest4 = Guest_List.pop()
print(f"\nMaaf {removed_guest4}, maaf aku tidak jadi mengundangmu ke acara dinner di rumahku.")
removed_guest5 = Guest_List.pop()
print(f"\nMaaf {removed_guest5}, maaf aku tidak jadi mengundangmu ke acara dinner di rumahku.")
removed_guest6 = Guest_List.pop()
print(f"\nMaaf {removed_guest6}, maaf aku tidak jadi mengundangmu ke acara dinner di rumahku.")

print()
print(f"Hello {Guest_List[0]}, ayo datang ke acara dinner di rumahku!")
print(f"Hello {Guest_List[1]}, ayo datang ke acara dinner di rumahku!")

del Guest_List[0]
del Guest_List[0]

print()
print(Guest_List)