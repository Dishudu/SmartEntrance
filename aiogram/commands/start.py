from bot_initialize import dp, bot
from aiogram import types
from aiogram.filters.command import Command

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Вот что я умею:\n"
        "- Отправьте изображение, чтобы сохранить его.\n"
        "- Используйте /list, чтобы увидеть список сохранённых изображений.\n"
        "- Используйте /delete <имя файла>, чтобы удалить изображение.")
    
    
    
    