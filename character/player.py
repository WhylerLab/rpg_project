# character/player.py

from character.base import Character


class Player(Character):
    def __init__(self, name, hp, attack, defense, gold=0):
        super().__init__(name, hp, attack, defense)
        self.gold = gold
        self.weapon_level = 1
        self.armor_level = 1