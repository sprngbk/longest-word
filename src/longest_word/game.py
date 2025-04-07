# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
"""This module defines the Game class for validating words based on a random letter grid."""

from collections import Counter
import random
import string
import requests

class Game:
    """Represents a word game with a 9-letter random grid."""
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = random.choices(string.ascii_uppercase, k=9)


    def is_valid(self, word: str) -> bool:
        """Check if the word can be formed using letters from the grid."""
        if not word:
            return False

        valid_word_response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json = valid_word_response.json()
        is_eng_word = json['found']

        if not is_eng_word:
            return False

        word_counter = Counter(word.upper())
        grid_counter = Counter(self.grid)

        for letter, count in word_counter.items():
            if count > grid_counter[letter]:
                return False

        return True
