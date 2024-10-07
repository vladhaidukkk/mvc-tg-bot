from aiogram.types import Message

from bot.abstractions.handlers import MessageHandler
from bot.builders.message import StartMessageBuilder


class StartCommandHandler(MessageHandler):
    def __init__(self) -> None:
        super().__init__(None, StartMessageBuilder())

    async def handle(self, message: Message) -> None:
        text, keyboard = self._builder.build(user=message.from_user)
        await message.answer(text=text, reply_markup=keyboard)
