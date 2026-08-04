# main.py complete game
from character.player import Player
from save.save_system import load_game

print("Mini RPG-Quest")
print("""1. Neues Spiel
2. Spielstand laden
3. Spiel beenden
""")
print()


player_choice = int(input("Wähle weise: "))

if player_choice == 1:
    name = input("Wie soll dein Held heißen: ")
    player = Player(name, 50, 15, 10)


elif player_choice == 2:
    daten = load_game()
    player = Player(daten["name"], daten["hp"], 15, 10)
    player.max_hp = daten["max_hp"]
    player.weapon.level = daten["weapon_level"]
    player.armor.level = daten["armor_level"]
    player.gold = daten["gold"]


elif player_choice == 3:
    exit()
