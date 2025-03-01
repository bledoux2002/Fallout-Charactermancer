# Creator class for Characters in the Fallout 2d20 Tabletop Roleplaying system by Modiphius Entertainment
# Created by Benjamin Ledoux using the Core Rulebook February 2023 edition.
# First created 2/28/2023 2230, last editted 2/26/2025 2240

import json

class Creator:
    def __init__(self, character):
        self.character = character

    def origin(self):
        pass

    def special(self):
        pass

    def skills(self):
        self.__tag_skills()
        pass

    def __tag_skills(self):
        pass

    def perk(self):
        pass

    def equipment(self):
        pass