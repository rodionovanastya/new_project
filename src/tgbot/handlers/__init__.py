from aiogram import Router, F
from aiogram.filters import Command, CommandStart


from .start import command_start


router: Router = Router(name=__name__)

@router.message(CommandStart())
async def cmd_start(message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()')
