# save/save_system.py

import json


def save_game(player, current_biome, fight_index, remaining_biomes):
    daten = {
        "name": player.name,
        "hp": player.hp,
        "max_hp": player.max_hp,
        "weapon_level": player.weapon.level,
        "armor_level": player.armor.level,
        "gold": player.gold,
        "current_biome": current_biome,
        "fight_index": fight_index,
        "remaining_biomes": remaining_biomes,
    }

    with open("saves/savegame.json", "w") as datei:
        json.dump(daten, datei)


def load_game():
    with open("saves/savegame.json", "r") as datei:
        daten = json.load(datei)
    return daten