from aiogram.types import Message

from bot.abstractions.handlers import MessageHandler
from bot.services.text import TextService


class MessagesFallbackHandler(MessageHandler):
    def __init__(self) -> None:
        super().__init__(TextService(), None)

    async def handle(self, message: Message) -> None:
        # TODO: Finish functionality implementation.
        await message.answer(":D")
