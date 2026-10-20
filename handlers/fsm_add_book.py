from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database import db

class Add_book(StatesGroup):
    book_id = State()
    name = State()
    author = State()
    genre = State()

router_add_book = Router()

@router_add_book.message(Command("add_book"))
async def start(message: Message, state: FSMContext):
    await message.answer("Введите номер книги: ")
    await state.set_state(Add_book.book_id)

@router_add_book.message(Add_book.book_id)
async def book_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Номер должен быть числом. Введите еще раз!")
        return
    else:
        await state.update_data(book_id = message.text)
    await message.answer("Введите название книги: ")
    await state.set_state(Add_book.name)

@router_add_book.message(Add_book.name)
async def name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите автора книги: ")
    await state.set_state(Add_book.author)

@router_add_book.message(Add_book.author)
async def author(message: Message, state: FSMContext):
    await state.update_data(author=message.text)
    await message.answer("Введите жанр книги: ")
    await state.set_state(Add_book.genre)

@router_add_book.message(Add_book.genre)
async def genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)

    data = await state.get_data()

    await message.answer("Данные книги\n"
                         f"Номер книги: {data['book_id']}\n"
                         f"Название книги: {data['name']}\n"
                         f"Автор книги: {data['author']}\n"
                         f"Жанр книги: {data['genre']}")

    await db.add_book(book_id=data['book_id'], name=data['name'], author=data['author'], genre=data['genre'])

    await state.clear()
    
