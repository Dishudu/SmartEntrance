from bot_initialize import dp, IMAGE_FOLDER
from .fsm_states import UploadImage
import os
from aiogram import F, types
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
import subprocess

@dp.message(commands=["restart_recognition"])
async def restart_recognition(message: Message):
    try:
        result = subprocess.run(
            ["supervisorctl", "restart", "face_recognition"],
            capture_output=True,
            text=True,
            check=True,
        )
        await message.answer(f"Процесс 'face_recognition' успешно перезапущен!\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        await message.answer(f"Ошибка при перезапуске процесса: {e.stderr}")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
