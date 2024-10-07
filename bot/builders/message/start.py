from aiogram.types import User
from aiogram.utils import markdown as md

from bot.abstractions.builders import MessageBuilder


class StartMessageBuilder(MessageBuilder):
    def build_message(self, user: User) -> str:
        return md.text(
            f"👋 Welcome, {md.hbold(user.full_name)}!",
            (
                f"Thank you for starting the {md.hbold('MVC Telegram Bot')}! "
                f"🤖 This bot is designed using the {md.hitalic('Model-View-Controller (MVC)')} architecture pattern, "
                "ensuring a well-organized and scalable code structure. "
                "📚 Whether you're here to explore its features or learn from its design, you're in the right place!"
            ),
            (
                "Feel free to interact with the bot to see how it works. "
                "🔍 If you have any questions or need assistance, don't hesitate to ask the admin. 💬"
            ),
            "Let's get started! 🚀",
            sep="\n\n",
        )
