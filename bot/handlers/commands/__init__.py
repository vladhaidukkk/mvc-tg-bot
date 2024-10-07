from aiogram import Router
from aiogram.filters import CommandStart

from .start import StartCommandHandler

router = Router(name=__name__)

start_command_handler = StartCommandHandler()
start_command_handler.register(router, CommandStart())
