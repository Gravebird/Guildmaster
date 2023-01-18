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
    