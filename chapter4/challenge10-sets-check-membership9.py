# Membership Testing using python sets

def membership_testing(book_set, book_to_check):
    return book_to_check in book_set

# Example usage:
books = {"Book1", "Book2", "Book3", "Book4"}

book_to_check1 = "Book2"
book_to_check2 = "Book5"

result1 = membership_testing(books, book_to_check1)
result2 = membership_testing(books, book_to_check2)

print(f"{book_to_check1} is in the set: {result1}")
print(f"{book_to_check2} is in the set: {result2}")
