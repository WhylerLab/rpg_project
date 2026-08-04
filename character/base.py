# character/base.py
from exceptions.custom_exceptions import HealLimitReachedError


class Character:
    """Basisklasse für alle Charaktere (Spieler und Gegner)."""


    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.defending = False
        self.heal_count = 6


    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp})"


    def take_damage(self, amount):
        if self.defending:
            amount = amount / 2
        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp = 0


    def heal(self, amount):
        if self.heal_count > 0:
            self.hp = self.hp + amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            self.heal_count -= 1
        else:
            raise HealLimitReachedError("Du hast keine Heilung mehr übrig.")

    def is_alive(self):
        return self.hp > 0