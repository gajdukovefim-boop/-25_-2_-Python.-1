disket_capacity_mb = 1.44
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4
chars_per_page = lines_per_page * chars_per_line
total_chars = chars_per_page * pages_per_book
book_size_bytes = total_chars * bytes_per_char
book_size_mb = book_size_bytes / (1024 * 1024)
books_count = int(disket_capacity_mb // book_size_mb)
print(f"Количество книг, помещающихся на дискету: {books_count}")
