import logging

import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from src.tgbot.config import Config, load_config
from src.tgbot.database.connect import create_async_engine_db, async_connection_db
from src.tgbot.middlewares import (
    SessionMiddleware,
    RegisteredMiddleware,
)
from src.tgbot.handlers import (
    router,
)


logger = logging.getLogger(__name__)


async def start_app(configfile):
    # -> Logging
    logging.basicConfig(
        format="[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
    )
    logger.debug("-> Bot online")

    # -> Config
    config: Config = load_config(configfile)

    # -> SQLAlchemy
    db_session = await async_connection_db(
        engine=await create_async_engine_db(
            config=config.db,
            echo=config.settings.sqlalchemy_echo,
        ),
        expire_on_commit=config.settings.sqlalchemy_expire_on_commit,
    )

    # -> BOT
    bot: Bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode='HTML')
    )
    dp: Dispatcher = Dispatcher(storage=MemoryStorage())

    # -> Middlewares
    dp.update.middleware(SessionMiddleware(sessionmaker=db_session))
    dp.update.middleware(RegisteredMiddleware())

    # -> Registerer Routers
    dp.include_router(router)

    # -> Start
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
    )