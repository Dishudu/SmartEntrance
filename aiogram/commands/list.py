from bot_initialize import dp, IMAGE_FOLDER
from .fsm_states import UploadImage
import os
from aiogram import F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

@dp.message(Command("list"))
async def list_images(message: types.Message):
    files = os.listdir(IMAGE_FOLDER)
    if not files:
        await message.answer("В папке нет сохранённых изображений.")
    else:
        file_list = "\n".join(files)
        await message.answer(f"Список сохранённых изображений:\n{file_list}")
