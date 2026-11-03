# 1. import module_name
import books
books.favorite_book('Laskar Pelangi')

# 2. from module_name import function_name
from books import favorite_book
favorite_book('Bumi Manusia')

# 3. from module_name import function_name as fn
from books import favorite_book as fb
fb('Cantik Itu Luka')

# 4. import module_name as mn
import books as bk
bk.favorite_book('Ronggeng Dukuh Paruk')

# 5. from module_name import *
# (tidak disarankan untuk program besar karena bisa bentrok nama)
from books import *
favorite_book('Pulang')