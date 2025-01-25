from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from pathlib import Path
import os
import logging
import configparser
from pathlib import Path
import sys

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
config.read(BASE_DIR / 'aiogram' / '.config')

BOT_TOKEN = config["Telegram"]["bot_token"]

logging.basicConfig(
    filename='bot_errors.log', 
    level=logging.ERROR,         
    format='%(asctime)s - %(levelname)s - %(message)s',
)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Папка для сохранения изображений
IMAGE_FOLDER = BASE_DIR / "shared" / "faces"

os.makedirs(IMAGE_FOLDER, exist_ok=True)
