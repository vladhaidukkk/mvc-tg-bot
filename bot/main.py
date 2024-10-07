import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.config import settings


async def main() -> None:
    dp = Dispatcher()

    bot = Bot(token=settings.bot.token)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
