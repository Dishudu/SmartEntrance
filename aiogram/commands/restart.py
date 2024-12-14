from bot_initialize import dp, IMAGE_FOLDER
from .fsm_states import UploadImage
import os
from aiogram import F, types
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
import docker

client = docker.from_env()

@dp.message(commands=["restart_recognition"])
async def restart_recognition(message: Message):
    try:
        container_name = "face_recognition"  # Имя контейнера с распознаванием лиц
        container = client.containers.get(container_name)
        container.restart()
        await message.answer("Контейнер с распознаванием лиц успешно перезапущен!")
    except Exception as e:
        await message.answer(f"Ошибка при перезапуске контейнера: {e}")

# Для supervisor
#
# @dp.message(commands=["restart_recognition"])
# async def restart_recognition(message: types.Message):
#     try:
#         subprocess.run(["supervisorctl", "restart", "face_recognition"], check=True)
#         await message.answer("Скрипт распознавания лиц успешно перезапущен!")
#     except subprocess.CalledProcessError as e:
#         await message.answer(f"Ошибка при перезапуске: {e}")