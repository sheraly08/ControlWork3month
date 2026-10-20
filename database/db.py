import aiosqlite
from database import queries
from config import path_db

async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.create_table)
        await conn.execute(queries.create_table_detail)
       
        await conn.commit()
    print('База данных успешно подключена!')

async def add_book(book_id, name, author, genre):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.insert_books, (book_id, name, author))
        await conn.execute(queries.insert_books_detail, (book_id, genre))
        await conn.commit()


async def get_books():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_books)
        books = await cursor.fetchall()
    return books