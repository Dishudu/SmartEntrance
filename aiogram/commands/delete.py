from bot_initialize import dp, IMAGE_FOLDER
from .fsm_states import UploadImage
import os
from aiogram import F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

@dp.message(Command("delete"))
async def delete_image(message: types.Message):
    command_parts = message.text.split(maxsplit=1)
    if len(command_parts) < 2:
        await message.answer("Укажите имя файла для удаления. Например: /delete example.jpg")
        return

    filename = command_parts[1]
    file_path = os.path.join(IMAGE_FOLDER, filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        await message.answer(f"Файл '{filename}' успешно удалён.")
    else:
        await message.answer(f"Файл '{filename}' не найден.")
        
        
        