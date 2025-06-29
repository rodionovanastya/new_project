from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types.message import Message

from .start import command_start


router: Router = Router(name=__name__)

@router.message()
async def cmd_start(message: Message):
    text = message.text
    print(text)
    await message.answer(f"Ты написал '{text}' и я это вижу! Проказник!")
