from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from database import db

router_commands = Router()

@router_commands.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Приветствую, {message.from_user.full_name}, я бот каталог-книг!\n"
                         "Команды: /add_book,"
                         "/books"
                         )

@router_commands.message(Command("books"))
async def get_books(message: Message):
    books = await db.get_books()


    if not books:
        await message.answer("В базе нет книг")
        return
    else:
        for book_id, name, author, genre in books:
            await message.answer("Данные книги\n"
                                     f"Номер книги: {book_id}\n"
                                     f"Название книги: {name}\n"
                                     f"Автор книги: {author}\n"
                                     f"Жанр книги: {genre}")



