# main.py complete game
from character.player import Player
from character.enemy import Enemy
from save.save_system import load_game, save_game
from world.biomes import get_random_biome_order
from world.enemy_data import ENEMY_DATA
from combat.engine import run_combat
import os

def main():
    # Menu
    print("=" * 40)
    print("       MINI RPG-QUEST")
    print("=" * 40)
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


    # Player Route
    player_walkthrough = get_random_biome_order()
    enemy_types = ["normal", "champion", "elite"]


    for biom in player_walkthrough:
        aktueller_index = player_walkthrough.index(biom)
        remaining_biomes = player_walkthrough[aktueller_index + 1:]
        print(f"\nDu betrittst: {biom.capitalize()}")

        for fight_index, typ in enumerate(enemy_types):
            enemy_data = ENEMY_DATA[biom][typ]

            while True:
                enemy = Enemy(enemy_data["name"], enemy_data["hp"], enemy_data["attack"], enemy_data["defense"], typ, enemy_data["flee_chance"], enemy_data["gold_reward"])
                print(f"\nEin {enemy.name} ({typ.capitalize()}) erscheint!")
                print(player)
                print("-" * 40)
                ergebnis = run_combat(player, enemy)

                if ergebnis == "sieg":
                    player.gold += enemy_data["gold_reward"]
                    print(f"Du erhältst {enemy_data['gold_reward']} Gold! (Gesamt: {player.gold})")

                    upgrade_wahl = input("Equipment verbessern? (w=Waffe, r=Rüstung, n=nein): ")
                    if upgrade_wahl == "w":
                        kosten = 20 * player.weapon.level
                        if player.gold >= kosten:
                            player.weapon.upgrade()
                            player.gold -= kosten
                            print(f"Waffe verbessert! Neue Stufe: {player.weapon.level}")
                        else:
                            print(f"Nicht genug Gold. Kosten: {kosten}, du hast: {player.gold}")
                    elif upgrade_wahl == "r":
                        kosten = 20 * player.armor.level
                        if player.gold >= kosten:
                            player.armor.upgrade()
                            player.gold -= kosten
                            print(f"Rüstung verbessert! Neue Stufe: {player.armor.level}")
                        else:
                            print(f"Nicht genug Gold. Kosten: {kosten}, du hast: {player.gold}")

                    speichern = input("Möchtest du speichern? (j/n): ")
                    if speichern == "j":
                        save_game(player, biom, fight_index, remaining_biomes)
                        print("Spielstand gespeichert.")

                if ergebnis == "niederlage":
                    try:
                        os.remove("saves/savegame.json")
                        print("Dein Spielstand wurde gelöscht.")
                    except FileNotFoundError:
                        pass
                    print("Deine Reise endet hier. Zurück zum Hauptmenü.")
                    return

                if ergebnis == "flucht":
                    print("Du versuchst dein Glück noch einmal...")
                else:
                    break

    print("\n" + "=" * 40)
    print(f"🎉 Glückwunsch, {player.name}! Du hast alle drei Biome überstanden!")
    print("=" * 40)


main()