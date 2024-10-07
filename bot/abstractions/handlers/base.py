from abc import ABC, abstractmethod

from aiogram import Router
from aiogram.dispatcher.event.handler import CallbackType

from bot.abstractions.builders.base import Builder
from bot.abstractions.service import Service


class Handler(ABC):
    def __init__(self, service: Service | None, builder: Builder | None) -> None:
        self._service = service
        self._builder = builder

    @abstractmethod
    async def handle(self, *args: any, **kwargs: any) -> None:
        pass

    @abstractmethod
    def register(self, router: Router, *filters: CallbackType) -> None:
        pass
