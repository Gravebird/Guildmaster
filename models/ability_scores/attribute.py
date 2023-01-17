

class Attribute:
    """
        An attribute that a creature has.

        Strength - Affects melee attacks and carrying capacity
        Dexterity - Affects armor class and ranged attacks
        Constitution - Affects health
        Intelligence - Affects spell damage
        Wisdom - Affects mana points
        Charisma - Affects how hard it is to resist spells
    """
    def __init__(self, attribute_name_, base_value_, damage_, drain_):

        self._list_of_possible_attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

        if self._list_of_possible_attributes.count(attribute_name_) == 0:
            # Attribute must have been spelled incorrectly
            # Ideally could use an enumerated type for this
            raise ValueError(f'{attribute_name_} does not exist in list [{self._list_of_possible_attributes}] - Likely a typo')
        
        self._base_value = base_value_
        self._attribute_damage = damage_
        self._attribute_drain = drain_
    

    def get_base_value(self):
        return self._base_value

    
    def get_current_value(self):
        """
            Calculates the current value of this attribute.
            It uses the base value and subtracts the damage and drain
            then needs to check equipped items and active buffs to find
            if there are any other modifiers.
        """
        return self._base_value - self._attribute_damage - self._attribute_drain