

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
        
        self._attribute_name = attribute_name_
        self._base_value = base_value_
        self._attribute_damage = damage_
        self._attribute_drain = drain_
    

    def get_base_value(self):
        return self._base_value

    def get_attribute_damage(self):
        return self._attribute_damage
    
    def get_attribute_drain(self):
        return self._attribute_drain

    def get_attribute_name(self):
        return self._attribute_name

    
    def get_current_value(self):
        """
            Calculates the current value of this attribute.
            It uses the base value and subtracts the damage and drain
            then needs to check equipped items and active buffs to find
            if there are any other modifiers.
        """
        return self._base_value - self._attribute_damage - self._attribute_drain

    
    def change_attribute_damage(self, amount):
        """
            Changes the attribute damage to this attribute by the amount specified.
            If a negative value is passed in, it will result in the attribute damage getting worse 
            (changing it by -1 will result in -1 to the attribute, not -1 to the damage)
        """
        self._attribute_damage += amount
        if self._attribute_damage < 0:
            self._attribute_damage = 0

    
    def change_attribute_drain(self, amount):
        """
            Changes the attribute drain to this attribute by the amount specified.
            If a negative value is passed in, it will result in the attribute drain getting worse
            (changing it by -1 will result in -1 to the attribute, not -1 to the damage)
        """
        self._attribute_drain += amount
        if self._attribute_drain < 0:
            self._attribute_drain = 0

    
    def get_modifier(self):
        """
            Calculates and returns the modifier for this ability score

            Formula is ([score] - 10) / 2 rounding down
        """
        return int((self.get_current_value() - 10) / 2)

    
    def to_json(self):
        """
            Used to save an attribute when saving to a file.
        """
        return {
            "base_value": self._base_value,
            "damage": self._attribute_damage,
            "drain": self._attribute_drain
        }