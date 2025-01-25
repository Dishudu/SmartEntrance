from commands import dp
from bot_initialize import bot
import asyncio

async def start_bot():
    try:   
        await dp.start_polling(bot)
        print("Бот запущен...")
        
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")
        
if __name__ == "__main__":
    asyncio.run(start_bot())