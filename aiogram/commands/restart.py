from bot_initialize import dp, IMAGE_FOLDER
from .fsm_states import UploadImage
import os
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
import subprocess

@dp.message(Command("restart"))
async def cmd_restart(message: types.Message):
    try:
        # Перезапуск через supervisorctl
        subprocess.run(["sudo", "supervisorctl", "restart", "face_recognition"], check=True)
        await message.answer("Процесс распознавания лиц успешно перезапущен.")
    except subprocess.CalledProcessError as e:
        await message.answer(f"Ошибка при перезапуске: {e}")