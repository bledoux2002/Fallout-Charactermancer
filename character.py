# Character file class for the Fallout 2d20 Tabletop Roleplaying system by Modiphius Entertainment
# Created by Benjamin Ledoux using the Core Rulebook February 2023 edition.
# First created 2/26/2023 2200, last editted 2/27/2025 0039

import json

class Character:
    def __init__(self, name="Wastelander"):
        self.name = name
        self.level = 1
        self.ap = 0
        self.xp = 0
        self.health = 0
        self.isRobot = False
        self.isNPC = False
        self.origin = None
        self.traits = {}
        self.equipmentPack = {}
        self.attributes = {
            "STR": 0,
            "PER": 0,
            "END": 0,
            "CHA": 0,
            "INT": 0,
            "AGI": 0,
            "LCK": 0
        }
        self.skills = {
            "Athletics": {"attribute": "STR"},
            "Barter": {"attribute": "CHA"},
            "Big Guns": {"attribute": "END"},
            "EnergyWeapons": {"attribute": "PER"},
            "Explosives": {"attribute": "PER"},
            "Lockpick": {"attribute": "PER"},
            "Medicine": {"attribute": "INT"},
            "MeleeWeapons": {"attribute": ""},
            "Pilot": {"attribute": "PER"},
            "Repair": {"attribute": "INT"},
            "Science": {"attribute": "INT"},
            "SmallGuns": {"attribute": "STR"},
            "Sneak": {"attribute": "AGI"},
            "Speech": {"attribute": "CHA"},
            "Surivival": {"attribute": "END"},
            "Throwing": {"attribute": "AGI"},
            "Unarmed": {"attribute": "STR"}
        }
        for skill in self.skills:
            skill["rank"] = 0
            skill["isTag"] = False
        self.perks = { # only difference from data.json is rank is single int instead of array
        """
        name: {
            rank: int,
            requirements: {
                levels: [],
                attributes: {
                    att: int
                },
                isRobot: bool
            },
            description: str
        }
        """
        }
        self.stats = {
            "carryWeight": 150, # base carry weight
            "damageResist": {
                "physical": 0,
                "energy": 0,
                "radiation": 0,
                "poison": 0
            },
            "defense": 0,
            "initiative": 0,
            "maxHealth": 0,
            "meleeBonus": 0
        }
        self.inventory = {
            "currency": {
                "caps": 0,
                "pre-war": 0,
                "gold": 0,
                "newMoney": 0,
                "scrip": 0
            },
            "gear": {
                "ammo": {},
                "armor": {},
                "clothing": {},
                "foodAndDrink": {},
                "chems": {},
                "otherConsumables": {},
                "weapons": {},
                "booksAndMags": {},
                "other": {}
            },
            "mods": {
                "armor": {},
                "clothing": {},
                "weapon": {},
                "robot": {}
            }
        }

    def update_special(self, attribute, value):
        """Update a SPECIAL attribute with a new value, and any derived statistics.

        Args:
            attribute (str): One of the seven SPECIAL attributes.
            value (int): New value of attribute, can be less.
        """
        if (self.attributes[attribute] != value):
            match (attribute):
                case "STR":
                    # Change by STR difference in new value, allows for homebrew modification of base carry weight
                    self.stats["carryWeight"] += (value - self.attributes[attribute]) * 10
                    if value > 10:
                        self.stats["meleeBonus"] = 3
                    elif value > 8:
                        self.stats["meleeBonus"] = 2
                    elif value > 6:
                        self.stats["meleeBonus"] = 1
                    else:
                        self.stats["meleeBonus"] = 0
                        
                case "PER":
                    self.stats["initiative"] += value - self.attributes[attribute]
                case "END":
                    self.stats["maxHealth"] += value - self.attributes[attribute]
                    if value > self.attributes[attribute]: # if increasing max health, increase current health by same amt
                        self.health += value - self.attributes[attribute]
                case "AGI":
                    self.stats["initiative"] += value - self.attributes[attribute]
                    if value < 9:
                        self.stats["defense"] = 1
                    else:
                        self.stats["defense"] = 2
                case "LCK":
                    self.stats["maxHealth"] += value - self.attributes[attribute]
                    if value > self.attributes[attribute]: # if increasing max health, increase current health by same amt
                        self.health += value - self.attributes[attribute]
            self.attributes[attribute] = value

    def xp_gain(self, gained):
        """Character has gained experience, add to total and handle possible level up.

        Args:
            gained (int): Number of experience points gained.

        Returns:
            int: 0, unless character has leveled up.
        """
        self.xp += gained
        while self.xp >= (self.level + 1) * (self.level / 2) * 100: # Core Rulebook, page 49
            self.level += 1
            self.stats["maxHealth"] += 1
            self.health += 1
            # INCREASE CHOSEN SKILL BY 1
            # CHOOSE NEW/UPGRADABLE PERK
            return 1
        return 0

    def eligible_perks(self):
        """List of all perks available to character at creation or when leveling up.

        Returns:
            (dict, dict): All perks character can take (or upgrade).
        """
        upgradable = {}
        new = {}

        for perk in self.perks:
            if self.__check_perk_requirements(perk):
                upgradable[perk] = self.perks[perk]
        
        perks = {}
        try:
            with open("data.json", "r", encoding="utf-8") as dataFile:
                perks = json.load(dataFile)["perks"]
        except:
            return 1

        for perk in perks:
            if perk not in self.perks:
                if self.__check_perk_requirements(perk):
                    new[perk] = self.perks[perk]

        return (upgradable, new)

    def __check_perk_requirements(self, perk):
        """Determine if character can take (or upgrade) a perk
        by looking through all requirements defined in data.json.

        Args:
            perk (str): Name of the perk being checked.

        Returns:
            bool: Whether the character fulfills the requirements of the perk.
        """
        reqsMet = False
        for req in perk["requirements"]:
            match (req):
                case "levels":
                    pass
                case "attributes":
                    pass
                case "isRobot":
                    pass
        
        return reqsMet