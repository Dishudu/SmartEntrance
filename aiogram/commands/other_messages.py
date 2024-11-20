from bot_initialize import dp, IMAGE_FOLDER
from .fsm_states import UploadImage
import os
from aiogram import F, types
from aiogram.fsm.context import FSMContext

# # Обработка других сообщений
# @dp.message(F.text, state="*")
# async def handle_other_messages(message: types.Message, state: FSMContext):
#     await message.answer("Отправьте изображение или документ для сохранения.")