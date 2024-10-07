from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router(name=__name__)


@router.message(CommandStart())
async def start_command_handler(message: Message) -> None:
    await message.answer(f"Hello {message.from_user.full_name}")
