# Character file class for the Fallout 2d20 Tabletop Roleplaying system by Modiphius Entertainment
# Created by Benjamin Ledoux using the Core Rulebook February 2023 edition.
# First created 2/26/2023 2200, last editted 2/28/2025 2230

import json

class Character:
    def __init__(self, name: str = "Wastelander"):
        self.name = name
        self.level = 1
        self.ap = 0
        self.xp = 0         # Enter number into field, set calls xp_gain(). If level up, pop up window asking if user wants to level
        self.hp = 0
        self.lp = 0
        self.isRobot = False
        self.isNPC = False
        self.origin = "NONE"
        self.trait = {
        }
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
        for _, skill in self.skills.items():
            skill["rank"] = 0
            skill["isTag"] = False
        # only difference from data.json is rank is single int instead of array
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
        self.perks = {
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
            "meleeBonus": 0,
            "maxLuck": 0,
            "maxAP": 6
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

    def info(self):
        print(f"{self.name}, level {self.level} {self.origin} ({self.xp} XP)")
        for att, val in self.attributes.items():
            print(f"{att}: {val}, ", end="")
        print(f"\n{self.hp} / " + str(self.stats["maxHealth"]) + " HP, ", end="")
        print(f"{self.ap} / " + str(self.stats["maxAP"]) + " AP, ", end="")
        print(f"{self.lp} / " + str(self.stats["maxLuck"]) + " Luck Points")

    def update_special(self, attribute, value):
        """Update a SPECIAL attribute with a new value, and any derived statistics.

        Args:
            attribute (str): One of the seven SPECIAL attributes.
            value (int): New value of attribute, can be less.
        """
        if (self.attributes[attribute] != value):
            dif = value - self.attributes[attribute]
            match (attribute):
                case "STR":
                    # Change by STR difference in new value, allows for homebrew modification of base carry weight
                    self.stats["carryWeight"] += dif * 10
                    if value > 10:
                        self.stats["meleeBonus"] = 3
                    elif value > 8:
                        self.stats["meleeBonus"] = 2
                    elif value > 6:
                        self.stats["meleeBonus"] = 1
                    else:
                        self.stats["meleeBonus"] = 0
                case "PER":
                    self.stats["initiative"] += dif
                case "END":
                    self.stats["maxHealth"] += dif
                    if value > self.attributes[attribute]: # if increasing max health, increase current health by same amt
                        self.hp += dif
                case "AGI":
                    self.stats["initiative"] += dif
                    if value < 9:
                        self.stats["defense"] = 1
                    else:
                        self.stats["defense"] = 2
                case "LCK":
                    self.stats["maxHealth"] += dif
                    if value > self.attributes[attribute]: # if increasing max health, increase current health by same amt
                        self.hp += dif
                    self.stats["maxLuck"] += dif
            self.attributes[attribute] = value

    def tag_skill(self, skill):
        self.skills[skill]["rank"] += 2
        if self.skills[skill]["rank"] > 6:
            self.skills[skill]["rank"] = 6
        self.skills[skill]["isTag"] = True

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
            self.hpMax += 1
            self.hp += 1
            # INCREASE CHOSEN SKILL BY 1
            # CHOOSE NEW/UPGRADABLE PERK
            return 1
        return 0

    def eligible_perks(self, perks):
        """List of all perks available to character at creation or when leveling up.

        Returns:
            (dict, dict): All perks character can take (or upgrade).
        """
        upgradable = {}
        new = {}

        for _, perk in self.perks.items():
            if self.__check_perk_requirements(perk):
                upgradable[perk] = self.perks[perk]
        
        perks = {}

        """
        Move file opening to editor.py
        When choosing a new perk, list all perks (expandable descriptions,
        perk "card" is a button, with a select button only clickable if a
        perk is chosen, ignorable popup window if ineligible for homebrew
        purposes, with settings allowing you to turn different warnings
        back on), have filters, including separate "upgradable" and
        "eligible" filter.
        """
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
        for req, _ in perk["requirements"].items():
            match (req):
                case "levels":
                    pass
                case "attributes":
                    pass
                case "isRobot":
                    pass
        
        return reqsMet

    def add_item(self, item):
        """Add equipment to inventory from data.json

        Args:
            item (dict): The item being added
        """
        # Need to figure out which tab in inventory to add item to, maybe item_field (currency, gear, mods) and item_type (caps, weapon, robot) args?


    # def update_ap(self, amt):
    #     """Change AP up to max, and increase max if Inspirational perk taken
    #     Not sure how to deal with increasing max if someone else in party takes perk,
    #     need to manually increase instead. Will wait until GUI finished since that migth affect approach.
    #     Maybe special context menu in menubar for this and similar situations?
    #     Buttons maybe deactivate when max/min, but if you manually enter higher number you can increase the max AP to that new value

    #     Args:
    #         amt (int): Total value to change current (and possibly max) AP totr, changeable from entry or plus/minus buttons (1 each)

    #     Returns:
    #         code (int): Success of operation, different numbners can mean different outcomes (0 succeeded, 1 failed (maxed out), 2 failed (too low))
    #     """
    #     self.