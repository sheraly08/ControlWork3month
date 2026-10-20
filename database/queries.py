

create_table = """
CREATE TABLE IF NOT EXISTS books (
id INTEGER  PRIMARY KEY AUTOINCREMENT,
book_id INTEGER NOT NULL UNIQUE,
name TEXT NOT NULL,
author TEXT NOT NUll

)

"""

insert_books = "INSERT INTO books (book_id, name, author) VALUES (?,?,?)"



create_table_detail = """
CREATE TABLE IF NOT EXISTS books_detail (
id INTEGER  PRIMARY KEY AUTOINCREMENT,
book_id INTEGER NOT NULL UNIQUE,
genre TEXT NOT NULL

)

"""


insert_books_detail = "INSERT INTO books_detail (book_id, genre) VALUES (?,?)"

get_books = """SELECT books.book_id, books.name, books.author, books_detail.genre 
FROM books INNER JOIN books_detail on books.book_id = books_detail.book_id """

