# world/enemy_data.py

ENEMY_DATA = {
    "friedhof": {
        "normal": {"name": "Skelett", "hp": 30, "attack": 8, "defense": 3, "flee_chance": 80, "gold_reward": 10},
        "champion": {"name": "Zombie", "hp": 45, "attack": 12, "defense": 5, "flee_chance": 50, "gold_reward": 20},
        "elite": {"name": "Lich", "hp": 60, "attack": 16, "defense": 8, "flee_chance": 20, "gold_reward": 40},
    },
    "wald": {
        "normal": {"name": "Wolf", "hp": 30, "attack": 8, "defense": 3, "flee_chance": 80, "gold_reward": 10},
        "champion": {"name": "Werwolf", "hp": 45, "attack": 12, "defense": 5, "flee_chance": 50, "gold_reward": 20},
        "elite": {"name": "Alpha Werwolf", "hp": 60, "attack": 16, "defense": 8, "flee_chance": 20, "gold_reward": 40},
    },
    "verlies": {
        "normal": {"name": "Ratte", "hp": 30, "attack": 8, "defense": 3, "flee_chance": 80, "gold_reward": 10},
        "champion": {"name": "Goblin", "hp": 45, "attack": 12, "defense": 5, "flee_chance": 50, "gold_reward": 20},
        "elite": {"name": "Oger", "hp": 60, "attack": 16, "defense": 8, "flee_chance": 20, "gold_reward": 40},
    },
}