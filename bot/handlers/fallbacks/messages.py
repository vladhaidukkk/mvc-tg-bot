from aiogram.types import Message

from bot.abstractions.handlers import MessageHandler
from bot.builders.message import TextStatsMessageBuilder
from bot.services import TextService


class MessagesFallbackHandler(MessageHandler):
    def __init__(self) -> None:
        super().__init__(TextService(), TextStatsMessageBuilder())

    async def handle(self, message: Message) -> None:
        words = self._service.cound_words(message.text)
        text, keyboard = self._builder.build(words=words)
        await message.reply(text=text, reply_markup=keyboard)
