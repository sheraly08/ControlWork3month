import asyncio
import logging
from config import bot, dp
from database import db
from handlers import echo, commands, fsm_add_book



async def main():
    await db.init_db()

    
    # регистрация обработчиков
    dp.include_router(commands.router_commands)
    dp.include_router(fsm_add_book.router_add_book)
   
    

    # Обработчик на ВСЁ 
    dp.include_router(echo.router_echo)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())