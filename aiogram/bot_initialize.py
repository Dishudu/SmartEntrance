from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from pathlib import Path
import os
import logging
import configparser
from pathlib import Path
import sys

config = configparser.ConfigParser()
PATH = Path(__file__).resolve().parent
config.read(str(PATH) + '/.config')

BOT_TOKEN = config["Telegram"]["bot_token"]

logging.basicConfig(
    filename='bot_errors.log',  # Имя файла для записи логов
    level=logging.ERROR,         # Уровень логирования
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат записи
)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Папка для сохранения изображений
IMAGE_FOLDER = "shared/faces"
os.makedirs(IMAGE_FOLDER, exist_ok=True)
