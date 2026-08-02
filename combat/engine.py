# combat/engine.py
from exceptions.custom_exceptions import InvalidActionError


def run_combat(player, enemy):
    while True:
        print("""1. Angriff (Leicht)
    2. Angriff (Schwer)
    3. Abwehr
    4. Heilung
    5. Flucht""")

        player_action = int(input("Was möchtest du tun: "))

        if player_action == 1:
            pass
        elif player_action == 2:
            pass
        elif player_action == 3:
            pass
        elif player_action == 4:
            pass
        elif player_action == 5:
            pass
        else:
            raise InvalidActionError()


        # 2. Falls Fliehen erfolgreich -> break (kein Gold, Kampf vorbei)

        # 3. Aktion ausführen (Schaden/Heilung/Abwehr)

        # 4. Gegner besiegt? -> break (Sieg)

        # 5. Gegner wählt Aktion (gewichtet)

        # 6. Gegner-Aktion ausführen

        # 7. Spieler besiegt? -> break (Niederlage)