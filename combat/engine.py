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


        if not enemy.is_alive():
            print(f"Du hast {enemy.name} besiegt!")
            break


        enemy_actions =[1, 2, 3, 4]
        enemy_weights=[40, 30, 20, 10]

        calledAction = random.choices(enemy_actions, weights=enemy_weights, k=1)[0]


        if calledAction == 1:
            schaden = enemy.attack
            player.take_damage(schaden)
            print (f"{enemy.name} greift mit leichten Angriff an. Du erleidest {schaden}")


        elif calledAction == 2:
            schaden = (enemy.attack)*1.5
            player.take_damage(schaden)
            print (f"{enemy.name} greift mit schweren Angriff an. Du erleidest {schaden}")


        elif calledAction == 3:
            enemy.defending = True
            print(f"{enemy.name} geht in die Verteidigung.")


        elif calledAction == 4:
            try:
                heilwert = enemy.max_hp * 0.25
                enemy.heal(heilwert)
                print(f"{enemy.name} heilt sich um {heilwert}")
            except HealLimitReachedError:
                print(f"{enemy.name} kann sich nicht mehr heilen.")


        if not player.is_alive():
            print("Deine Reise hat ein jähes Ende erlitten.")
            break


        player.defending = False
        enemy.defending = False