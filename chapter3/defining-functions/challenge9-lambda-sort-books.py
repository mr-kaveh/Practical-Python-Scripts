# List of dictionaries representing books
books = [
    {"title": "Harry Potter", "author": "J.K. Rowling", "pages": 336},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "pages": 281},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": 180},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "pages": 279},
]

# Sort books by title in ascending order using a lambda function
sorted_books_by_title = sorted(books, key=lambda book: book["title"])
print("Books sorted by title (ascending):")
for book in sorted_books_by_title:
    print(f"{book['title']} by {book['author']} ({book['pages']} pages)")

# Sort books by the number of pages in descending order using a lambda function
sorted_books_by_pages = sorted(books, key=lambda book: book["pages"], reverse=True)
print("\nBooks sorted by pages (descending):")
for book in sorted_books_by_pages:
    print(f"{book['title']} by {book['author']} ({book['pages']} pages)")
