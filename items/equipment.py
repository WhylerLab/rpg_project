# items/equipment.py

class Equipment:
    """Basisklasse für alle Ausrüstungsgegenstände (Waffe, Rüstung)."""

    def __init__(self, name, level=1, max_level=5):
        self.name = name
        self.level = level
        self.max_level = max_level

    def upgrade(self):
        if self.level == self.max_level:
            print("Maximale Upgradestufe erreicht +5")
        else:
            self.level += 1 # Level um 1 erhöhen, aber nicht über max_level


class Weapon(Equipment):
    def __init__(self, name, base_attack):
        super().__init__(name, level=1, max_level=5)
        self.base_attack = base_attack

    def get_attack_bonus(self):
        bonus = self.base_attack * self.level # Angriffsbonus basierend auf aktuellem Level berechnen
        return bonus

class Armor(Equipment):
    def __init__(self, name, base_defense):
        super().__init__(name, level=1, max_level=5)
        self.base_defense = base_defense

    def get_defense_bonus(self):
        bonus = self.base_defense * self.level # Verteidigungsbonus basierend auf aktuellem Level berechnen
        return bonus