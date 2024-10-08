from collections import Counter

from aiogram.utils import markdown as md

from bot.abstractions.builders import MessageBuilder


class TextStatsMessageBuilder(MessageBuilder):
    def build_message(self, words: Counter[str, int]) -> str:
        return md.text(*[f"{md.hbold(word)}: {count}" for word, count in words.items()], sep="\n")
