from abc import ABC, abstractmethod

from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup


class Message(ABC):
    def build(self, *args: any, **kwargs: any) -> tuple[str, ReplyKeyboardMarkup | InlineKeyboardMarkup | None]:
        return self.build_message(*args, **kwargs), self.build_keyboard(*args, **kwargs)

    @abstractmethod
    def build_message(self, *args: any, **kwargs: any) -> str:
        pass

    @abstractmethod
    def build_keyboard(self, *args: any, **kwargs: any) -> ReplyKeyboardMarkup | InlineKeyboardMarkup | None:
        return None
