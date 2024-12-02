from bot_initialize import dp, IMAGE_FOLDER
from .fsm_states import UploadImage
import os
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
import subprocess

@dp.message(commands=["restart_recognition"])
async def restart_recognition(message: types.Message):
    try:
        subprocess.run(["supervisorctl", "restart", "face_recognition"], check=True)
        await message.answer("Скрипт распознавания лиц успешно перезапущен!")
    except subprocess.CalledProcessError as e:
        await message.answer(f"Ошибка при перезапуске: {e}")