# character/enemy.py

from character.base import Character


class Enemy(Character):
    def __init__(self, name, hp, attack, defense, enemy_type, flee_chance, gold_reward=0):
        super().__init__(name, hp, attack, defense)
        self.enemy_type = enemy_type
        self.flee_chance = flee_chance
        self.gold_reward = gold_reward