import models.utilities.dice as dice

from models.ability_scores.attribute import Attribute

class Ability_Score_Bundle:
    """
        A group of 6 ability scores

        Strength
        Dexterity
        Constitution
        Intelligence
        Wisdom
        Charisma
    """
    def __init__(self):
        self._strength = Attribute("Strength", 
            roll_ability_score_for_hero(),
            0,0)
        self._dexterity = Attribute("Dexterity",
            roll_ability_score_for_hero(),
            0,0)
        self._constitution = Attribute("Constitution",
            roll_ability_score_for_hero(),
            0,0)
        self._intelligence = Attribute("Intelligence",
            roll_ability_score_for_hero(),
            0,0)
        self._wisdom = Attribute("Wisdom",
            roll_ability_score_for_hero(),
            0,0)
        self._charisma = Attribute("Charisma",
            roll_ability_score_for_hero(),
            0,0)
    

    def print_stats(self):
        print(f'Str: {self._strength.get_current_value()} ({self._strength.get_modifier()})')
        print(f'Dex: {self._dexterity.get_current_value()} ({self._dexterity.get_modifier()})')
        print(f'Con: {self._constitution.get_current_value()} ({self._constitution.get_modifier()})')
        print(f'Int: {self._intelligence.get_current_value()} ({self._intelligence.get_modifier()})')
        print(f'Wis: {self._wisdom.get_current_value()} ({self._wisdom.get_modifier()})')
        print(f'Cha: {self._charisma.get_current_value()} ({self._charisma.get_modifier()})')

    
    def to_json(self):
        """
            Used to save this ability score bundle to a file.
        """
        return {
            "strength": self._strength.to_json(),
            "dexterity": self._dexterity.to_json(),
            "constitution": self._constitution.to_json(),
            "intelligence": self._intelligence.to_json(),
            "wisdom": self._wisdom.to_json(),
            "charisma": self._charisma.to_json()
        }

    
    def from_json(self, json):
        """
            Used to load this ability score bundle from a file.
        """
        self._strength = Attribute("Strength",json["strength"]["base_value"],
            json["strength"]["damage"], json["strength"]["drain"])
        self._dexterity = Attribute("Dexterity",json["dexterity"]["base_value"],
            json["dexterity"]["damage"],json["dexterity"]["drain"])
        self._constitution = Attribute("Constitution",json["constitution"]["base_value"],
            json["constitution"]["damage"], json["constitution"]["drain"])
        self._intelligence = Attribute("Intelligence",json["intelligence"]["base_value"],
            json["intelligence"]["damage"], json["intelligence"]["drain"])
        self._wisdom = Attribute("Wisdom",json["wisdom"]["base_value"],
            json["wisdom"]["damage"], json["wisdom"]["drain"])
        self._charisma = Attribute("Charisma",json["charisma"]["base_value"],
            json["charisma"]["damage"], json["charisma"]["drain"])


def roll_ability_score_for_hero():
    """
        Rolls 4d6 dropping the worst roll, then adds the modifier to
        it.
    """
    rolls = []
    total = 0
    for i in range(4):
        num = dice.roll_d6()
        total += num
        rolls.append(num)
    
    low_roll = min(rolls)
    total -= low_roll
    rolls.remove(low_roll)

    return total
    