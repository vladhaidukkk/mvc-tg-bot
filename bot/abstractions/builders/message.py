from abc import ABC, abstractmethod

from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup

from .base import Builder


class MessageBuilder(Builder, ABC):
    def build(self, *args: any, **kwargs: any) -> tuple[str, ReplyKeyboardMarkup | InlineKeyboardMarkup | None]:
        return self.build_message(*args, **kwargs), self.build_keyboard(*args, **kwargs)

    @abstractmethod
    def build_message(self, *args: any, **kwargs: any) -> str:
        pass

    def build_keyboard(self, *args: any, **kwargs: any) -> ReplyKeyboardMarkup | InlineKeyboardMarkup | None:  # noqa: ARG002
        return None
