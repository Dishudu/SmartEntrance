from commands import dp
from bot_initialize import bot
import asyncio

# Запуск бота
async def start_bot():
    try:   
        # Запуск асинхронного polling
        await dp.start_polling(bot)
        print("Бот запущен...")
        
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")
        
if __name__ == "__main__":
    # Запускаем бота с помощью asyncio
    asyncio.run(start_bot())