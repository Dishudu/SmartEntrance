from aiogram import F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from bot_initialize import dp, bot, IMAGE_FOLDER
from .fsm_states import UploadImage
import os

@dp.message(F.photo)
async def handle_photo(message: types.Message, state):
    # Получаем файл изображения
    photo = message.photo[-1]  # Берем изображение с максимальным разрешением
    file = await bot.get_file(photo.file_id)

    # Скачиваем файл
    temp_path  = os.path.join(IMAGE_FOLDER, f"{message.from_user.id}_{photo.file_id}.jpg")
    await bot.download_file(file.file_path, temp_path)
    
    # Сохраняем путь к файлу в состоянии
    await state.update_data(temp_path=temp_path)
    
    await message.answer("Фото загружено. Введите имя для файла:")
    await state.set_state(UploadImage.waiting_for_name)
    print(f"Фото сохранено: {temp_path}")

@dp.message(F.document & F.document.mime_type.in_({"image/jpeg"}))
async def handle_document(message: types.Message, state):
    # Если пользователь отправил изображение как документ
    document = message.document
    file = await bot.get_file(document.file_id)

    file_extension = document.file_name.split(".")[-1]
    temp_path = os.path.join(IMAGE_FOLDER, f"{message.from_user.id}_{document.file_id}.{file_extension}")
    await bot.download_file(file.file_path, temp_path)
    
    await state.update_data(temp_path=temp_path)

    await message.answer("Фото загружено. Введите имя для файла:")
    await state.set_state(UploadImage.waiting_for_name)
    print(f"Изображение сохранено: {temp_path}")
