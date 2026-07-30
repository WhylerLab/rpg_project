# Mini RPG — Terminal Edition

Rundenbasiertes Terminal-RPG in reinem Python (keine externen Frameworks für die Logik).
Entstanden als Lernprojekt parallel zur PCAP-Zertifizierungsvorbereitung.

## Konzept

Ein Held zieht durch drei Biome, kämpft rundenbasiert gegen zufällige Gegner
und verbessert seine Ausrüstung mit erbeutetem Gold. Kein Level-System, kein
Item-Chaos — Fokus liegt auf sauberer Spiellogik statt Umfang.

Details zur vollständigen Spezifikation: siehe [`docs/PROJECT_PLAN.md`](docs/PROJECT_PLAN.md).

## Status

🚧 In Entwicklung — Grundgerüst steht, Implementierung folgt modulweise.

## Setup

```bash
git clone <repo-url>
cd rpg_project
python3 main.py
```

Keine externen Abhängigkeiten (siehe `requirements.txt`).

## Projektstruktur

```
rpg_project/
├── main.py                  # Einstiegspunkt, Game-Loop
├── character/
│   ├── base.py               # Character-Basisklasse
│   ├── player.py             # Player(Character)
│   └── enemy.py               # Enemy(Character)
├── combat/
│   └── engine.py              # Rundenbasierte Kampflogik
├── items/
│   └── equipment.py           # Waffe/Rüstung, Upgrade-System
├── world/
│   ├── biomes.py               # Biom-Definitionen & Reihenfolge
│   └── enemy_data.py           # Gegnerrassen pro Biom
├── save/
│   └── save_system.py          # JSON speichern/laden
├── exceptions/
│   └── custom_exceptions.py    # Eigene Exception-Hierarchie
├── saves/                     # Speicherstände (nicht versioniert)
└── docs/
    └── PROJECT_PLAN.md         # Vollständige Spielspezifikation
```

## Später geplant

- Pygame-GUI-Version auf Basis der bestehenden Logikschicht
