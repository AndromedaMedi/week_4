from models.book import Book
from models.author import Author

from repositories import book_repository
from repositories import author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Stephen Hawkin")
author_repository.save(author1)
author2 = Author("Eckhart Tolle")
author_repository.save(author2)
author3 = Author("John C. Parkin")
author_repository.save(author3)

book1 = Book("Brief Answers to the Big Questions", 2020, author1)
book_repository.save(book1)
book2 = Book("The Power of Now", 2001, author2)
book_repository.save(book2)
book3 = Book("F**k It: The Untimate Spiritual Way", 2008, author3)
book_repository.save(book3)
