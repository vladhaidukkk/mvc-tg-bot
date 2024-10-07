from aiogram.types import User
from aiogram.utils import markdown as md

from bot.abstractions.builders import MessageBuilder


class StartMessageBuilder(MessageBuilder):
    def build_message(self, user: User) -> str:
        return md.text(
            f"👋 Welcome, {md.hbold(user.full_name)}!",
            (
                f"Thank you for starting the {md.hbold('MVC Telegram Bot')}! "
                "🤖 This bot is designed to analyze your text inputs. "
                f"It is built following the {md.hitalic('Model-View-Controller (MVC)')} architecture pattern, ensuring "
                "a scalable and maintainable codebase. 📚"
            ),
            "Simply send any text, and I'll provide insights and analysis based on your input!",
            "If you have any questions or need assistance, don't hesitate to ask the admin. 💬",
            "Let's get started! 🚀",
            sep="\n\n",
        )
