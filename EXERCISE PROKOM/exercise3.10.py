mountains = ['merapi', 'rinjani', 'semeru', 'kerinci', 'bromo']
print("List awal:")
print(mountains)
print(f"\nGunung pertama dari daftar adalah {mountains[0].title()}.")
print(f"Gunung terakhir dari daftar adalah {mountains[-1].title()}.")

mountains[0] = 'sumbing'
print("\nSetelah mengganti gunung pertama:")
print(mountains)    

mountains.append('lawu')
mountains.insert(2, 'slamet')
print("\nSetelah menambahkan gunung baru:")
print(mountains)

del mountains[3]
print("\nSetelah menghapus gunung keempat:")
print(mountains)

popped_mountain = mountains.pop()
print(f"\nPoppped {popped_mountain.title()} dari awal daftar.")
print(mountains)

print(f"\nPopped {popped_mountain.title()} dari akhir daftar.")
print(mountains)

mountains.remove('kerinci')
print("\nSetelah menghapus gunung kerinci:")
print(mountains)    

mountains.append('agung')
mountains.append('raung')
mountains.append('guntur')
print("\nDaftar Terbaru:")
print(mountains)

print("\nSorted sementara oleh sorted:")
print(sorted(mountains))
print("\nReverse Sorted:")
print(sorted(mountains, reverse=True))
print("Original list:")
print(mountains)

mountains.reverse()
print("Setelah list direserve:")
print(mountains)

mountains.sort()
print("Setelah sort:")
print(mountains)

mountains.sort(reverse=True)
print("List setelah sort reverse:")
print(mountains)

print(f"\nTotal ada {len(mountains)} dari daftar.")