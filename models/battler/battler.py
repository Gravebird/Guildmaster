

class Battler:
    """
        An abstract class to represent some creature that can
        do battle in this game.
    """
    def __init__(self, max_hp_):
        self._max_hp = max_hp_
        self._current_hp = max_hp_
    

    def get_max_hp(self):
        return self._max_hp
    

    def get_current_hp(self):
        return self._current_hp