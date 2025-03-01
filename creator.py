# Creator class for Characters in the Fallout 2d20 Tabletop Roleplaying system by Modiphius Entertainment
# Created by Benjamin Ledoux using the Core Rulebook February 2023 edition.
# First created 2/28/2023 2230, last editted 2/26/2025 2240

import json

class Creator:
    def __init__(self, character):
        self.character = character
        self.data = {}
        with open("data.json", "r", encoding="utf-8") as dataFile:
            self.data = json.load(dataFile)

    def origin(self):
        pass

    def special(self):
        for attribute in self.character.attributes:
            self.character.update_special(attribute, 5)

    def skills(self, tagged, ranks):
        for skill in tagged:
            self.character.tag_skill(skill)

        for skill, rank in ranks:
            self.character.skills[skill] = rank

    def perk(self):
        pass

    def equipment(self):
        pass