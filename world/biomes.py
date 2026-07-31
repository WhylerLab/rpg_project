# world/biomes.py

import random

BIOME_ORDER = ["friedhof", "wald", "verlies"]


def get_random_biome_order():
    walkthrough = random.sample(BIOME_ORDER, k=3) # Kopie der Liste zufällig mischen und zurückgeben
    return(walkthrough)