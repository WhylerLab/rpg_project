# combat/engine.py

from exceptions.custom_exceptions import InvalidActionError, HealLimitReachedError
import random

def run_combat(player, enemy):
    while True:
        print(f"""Kampfaktion wählen:
    1. Angriff (Leicht)
    2. Angriff (Schwer)
    3. Abwehr
    4. Heilung ({player.heal_count} übrig)
    5. Flucht""")

        player_action = int(input("Was möchtest du tun: "))

        if player_action == 1:
            schaden = player.attack + player.weapon.get_attack_bonus()
            enemy.take_damage(schaden)
            print (f"Du greifst mit einem leichten Angriff an. {enemy.name} erleidet {schaden}")

        elif player_action == 2:
            schaden = (player.attack + player.weapon.get_attack_bonus())*1.5
            enemy.take_damage(schaden)
            print (f"Du greifst mit einem schweren Angriff an. {enemy.name} erleidet {schaden}")

        elif player_action == 3:
            player.defending = True
            print("Du gehst in die Verteidigung.")

        elif player_action == 4:
            try:
                heilwert = player.max_hp * 0.5
                player.heal(heilwert)
                print(f"Du hast dich um {heilwert} geheilt! Nur noch {player.heal_count} übrig!")
            except HealLimitReachedError:
                print("Du hast keine Heilung mehr übrig.")


        elif player_action == 5:
            print("Du versuchst zu flüchten.")
            flee_throw = random.randint(1, 100)
            if flee_throw <= enemy.flee_chance:
                print("Flucht ist geglückt!")
                break
            else:
                print("Flucht ist gescheitert!")
            
        else:
            raise InvalidActionError()


        # 2. Falls Fliehen erfolgreich -> break (kein Gold, Kampf vorbei)

        # 3. Aktion ausführen (Schaden/Heilung/Abwehr)

        # 4. Gegner besiegt? -> break (Sieg)

        # 5. Gegner wählt Aktion (gewichtet)

        # 6. Gegner-Aktion ausführen

        # 7. Spieler besiegt? -> break (Niederlage)

        player.defending = False
        enemy.defending = False