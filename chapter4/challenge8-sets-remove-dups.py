# removes duplicates from list of books

def remove_duplicates(book_list):
    unique_books = list(set(book_list))
    return unique_books

# Example usage:
books = ["Book1", "Book2", "Book1", "Book3", "Book2"]
unique_books = remove_duplicates(books)
print(unique_books)

