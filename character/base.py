# character/base.py

class Character:
    """Basisklasse für alle Charaktere (Spieler und Gegner)."""


    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense


    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp})"


    def take_damage(self, amount):
        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp = 0


    def heal(self, amount):
        self.hp = self.hp + amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp


    def is_alive(self):
        return self.hp > 0