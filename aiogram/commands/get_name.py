from bot_initialize import dp, IMAGE_FOLDER
from .fsm_states import UploadImage
import os
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter

@dp.message(StateFilter(UploadImage.waiting_for_name))
async def handle_name(message: types.Message, state: FSMContext):
    # Получаем данные из состояния
    data = await state.get_data()
    temp_path = data.get("temp_path")

    # Имя файла от пользователя
    user_filename = message.text.strip()
    if not user_filename:
        await message.answer("Имя файла не может быть пустым. Попробуйте снова.")
        return

    # Формируем путь для сохранения файла
    extension = os.path.splitext(temp_path)[1]  # Сохраняем оригинальное расширение
    final_path = os.path.join(IMAGE_FOLDER, f"{user_filename}{extension}")

    # Переименовываем файл
    os.rename(temp_path, final_path)

    await message.answer(f"Файл успешно сохранён как: {user_filename}{extension}")

    # Очистка состояния
    await state.clear()