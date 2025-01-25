from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

class UploadImage(StatesGroup):
    waiting_for_image = State()
    waiting_for_name = State()
    