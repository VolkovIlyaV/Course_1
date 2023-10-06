# TODO Найдите количество книг, которое можно разместить на дискете
floppy_disk_capacity_mb = 1.44     # Известные значения
pages = 100
lines = 50
symbol = 25
symbol_volume_byte = 4

floppy_disk_capacity_byte = floppy_disk_capacity_mb * 1024 * 1024   # Расчёт объёма дискеты в байтах

book_volume_byte = pages * lines * symbol * symbol_volume_byte      # Расчёт объёма книги в байтах

number_of_books_on_a_floppy_disk_ = floppy_disk_capacity_byte // book_volume_byte   # Расчёт количества книг
number_of_books_on_a_floppy_disk = int(number_of_books_on_a_floppy_disk_)   # Переод значения из float в int

print("Количество книг, помещающихся на дискету:", number_of_books_on_a_floppy_disk)
