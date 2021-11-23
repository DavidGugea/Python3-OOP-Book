from collections import namedtuple

Book = namedtuple("Book", "author title genre")
books = [
    Book("Author 1", "Title 1", "Genre 1"),
    Book("Author 2", "Title 2", "Genre 1"),
    Book("Author 3", "Title 3", "Genre 2"),
    Book("Author 4", "Title 4", "Genre 2"),
    Book("Author 5", "Title 5", "Genre 3"),
    Book("Author 6", "Title 6", "Genre 3"),
    Book("Author 7", "Title 7", "Genre 4")
]

genre_3_authors = {b.title: b for b in books if b.genre == "Genre 3"}
print(genre_3_authors)
