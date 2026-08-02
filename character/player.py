# character/player.py

from character.base import Character
from items.equipment import Weapon, Armor


class Player(Character):
    def __init__(self, name, hp, attack, defense, gold=0):
        super().__init__(name, hp, attack, defense)
        self.gold = gold
        self.weapon = Weapon("Schwert", 15)
        self.armor = Armor("Rüstung", 10)