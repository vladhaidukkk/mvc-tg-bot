from abc import ABC, abstractmethod

from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup

from bot.builders.base import BaseBuilder


class BaseMessageBuilder(BaseBuilder, ABC):
    @abstractmethod
    def build(*args: any, **kwargs: any) -> tuple[str, ReplyKeyboardMarkup | InlineKeyboardMarkup]:
        pass
