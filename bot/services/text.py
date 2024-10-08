from collections import Counter
from string import punctuation

from bot.abstractions.service import Service


class TextService(Service):
    def cound_words(self, text: str) -> Counter:
        words = [part.strip(punctuation) for part in text.lower().split()]
        return Counter(words)
