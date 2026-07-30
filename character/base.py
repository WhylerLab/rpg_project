# character/base.py

class Character:
    """Basisklasse für alle Charaktere (Spieler und Gegner)."""

    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense

    def take_damage(self, amount):
        # HP reduzieren, dabei nicht unter 0 fallen lassen
        pass

    def heal(self, amount):
        # HP erhöhen, dabei nicht über max_hp steigen lassen
        pass

    def is_alive(self):
        # True/False je nach aktuellem HP-Stand
        pass