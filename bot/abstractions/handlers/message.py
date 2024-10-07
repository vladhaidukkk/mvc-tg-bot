from abc import ABC

from aiogram import Router
from aiogram.dispatcher.event.handler import CallbackType

from bot.abstractions.builders import MessageBuilder
from bot.abstractions.service import Service

from .base import Handler


class MessageHandler(Handler, ABC):
    def __init__(self, service: Service | None, message_builder: MessageBuilder | None) -> None:
        super().__init__(service=service, builder=message_builder)

    def register(self, router: Router, *filters: CallbackType) -> None:
        router.message(*filters)(self.handle)
