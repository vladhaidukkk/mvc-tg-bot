from aiogram import Router
from aiogram.filters import CommandStart

from .messages import MessagesFallbackHandler

router = Router(name=__name__)

messages_fallback_handler = MessagesFallbackHandler()
messages_fallback_handler.register(router)
