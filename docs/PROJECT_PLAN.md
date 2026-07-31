# Projektplan — Mini RPG (Terminal Edition)

## 1. Spielkonzept

Der Spieler durchläuft in einem Durchlauf alle drei Biome in **zufälliger
Reihenfolge**. Pro Biom finden **3 Kämpfe** gegen generierte Gegner
statt. Nach jedem gewonnenen Kampf wird gefragt, ob gespeichert werden soll.

## 2. Biome & Gegner

**Der Gegnertyp legt direkt den Namen fest** — pro Biom gibt es genau
**3 feste Gegner**, je einen pro Typ (keine 3×3-Matrix, keine separate
"Rasse"). Beispiel Friedhof:

| Typ | Name (Beispiel) | Statmultiplikator | Fluchtchance des Spielers dagegen |
|---|---|---|---|
| Normal | Skelett | 1.0x | 80% |
| Champion | Zombie | 1.5x (Platzhalter, anpassbar) | 50% |
| Elite | TBD (Spezialname) | 2.0x (Platzhalter, anpassbar) | 20% |

| Biom | Normal | Champion | Elite |
|---|---|---|---|
| Friedhof | Skelett | Zombie | Lich |
| Düsterer Wald | Wolf | Werwolf | Alpha-Werwolf |
| Dunkles Verließ | Ratte | Goblin | Oger |

Champion/Elite nutzen dieselben 4 Aktionen wie Normal-Gegner — keine
Sonderangriffe, nur stärkere Werte.

**Kampfreihenfolge innerhalb eines Bioms:** fest aufsteigend —
Normal → Champion → Elite (kein Zufall). Zufällig ist ausschließlich die
**Reihenfolge der drei Biome** im Gesamtdurchlauf.

## 3. Kampfsystem

Rundenbasiert. Pro Runde wählt jede Partei eine Aktion:

- **Angriff (leicht)** — geringerer Schaden, (höhere Trefferchance, optional)
- **Angriff (schwer)** — höherer Schaden, (geringere Trefferchance, optional)
- **Abwehr** — reduziert eingehenden Schaden in der Folgerunde
- **Heilung** — stellt HP wieder her, **max. 2× pro Kampf**, gilt für Spieler
  UND Gegner gleichermaßen

Zusätzlich nur für den Spieler:

- **Wegrennen** — Erfolgschance abhängig vom Gegnertyp (80/50/20%). Bei
  Erfolg wird der Kampf abgebrochen, bei Misserfolg verliert der Spieler die
  Runde (Gegner handelt regulär).

### Gegner-KI (Aktionswahl)

Der Gegner wählt seine Aktion pro Runde zufällig, aber **gewichtet** über
`random.choices(..., weights=...)` — nicht gleichverteilt, da sonst z. B.
Heilung trotz Limit (max. 2×) zu oft gezogen würde. Grober Ansatz:

```python
import random

action = random.choices(
    ["attack_light", "attack_heavy", "defend", "heal"],
    weights=[40, 30, 20, 10],   # Platzhalter, anpassbar
    k=1,
)[0]
```

Heilung fällt aus der Auswahl raus, sobald das Limit (2× pro Kampf) erreicht
ist — das Gewichtungs-Array muss dann entsprechend ohne "heal" neu
zusammengestellt werden (oder Gewicht auf 0 setzen und neu normalisieren).
Exakte Gewichtungswerte sind noch Platzhalter, siehe offene Punkte unten.

### Rundenreihenfolge

Der Spieler handelt in jeder Runde zuerst, danach reagiert der Gegner
(sequenziell, nicht simultan). D. h. z. B. eine Abwehr des Spielers wirkt
noch in derselben Runde gegen den nachfolgenden Gegnerangriff.

## 3a. Niederlage & Sieg

**Niederlage** (Spieler-HP fällt auf 0): Game-Over-Meldung, danach Angebot,
den letzten Spielstand zu laden. Kein automatischer Neustart.

**Sieg** (alle 3 Biome / 9 Kämpfe abgeschlossen): Abschlussmeldung an den
Spieler. Kein weiterer Mechanismus (z. B. kein Score-Screen) vorgesehen —
kann bei Bedarf später ergänzt werden.

## 3b. Programmstart

Beim Start von `main.py` genau zwei Optionen, kein weiteres Menü:

1. Neues Spiel
2. Letzten Spielstand laden

Falls kein Spielstand existiert, entfällt Option 2 entsprechend (oder gibt
eine Fehlermeldung/Hinweis aus, statt einen leeren Ladevorgang zu erlauben).

## 4. Progression

Kein Level-System. Fortschritt ausschließlich über Ausrüstung:

- Gegner droppen **nur Gold** (kein EP, kein Item-Loot)
- Waffe und Rüstung sind **getrennt** upgradebar, jeweils **+1 bis +5**
- Waffen-Upgrade erhöht Angriffswert, Rüstungs-Upgrade erhöht Verteidigung
- Upgrade-Kosten: TBD (z. B. linear oder exponentiell steigend pro Stufe)

## 5. Speichersystem

- Kein separates Menü nötig
- Nach jedem **gewonnenen** Kampf: Abfrage "Speichern? (j/n)"
- Speicherformat: JSON, enthält mind.:
  - Spieler-HP/Max-HP
  - Waffen-/Rüstungsstufe
  - Gold
  - Fortschritt (aktuelles Biom, Kampf-Index innerhalb des Bioms)
  - Reihenfolge der verbleibenden Biome

## 6. Offene Designentscheidungen (bewusst noch nicht festgelegt)

- [ ] Konkrete Namen der Elite-Gegner (3x, ein "Spezialname" pro Biom)
- [ ] Konkrete Namen für Wald- und Verließ-Gegner (Normal/Champion; Friedhof
      bereits klar: Skelett/Zombie)
- [ ] Konkrete Basis-Stats pro Gegner (HP, Angriff, Verteidigung)
- [ ] Exakte Schadensformeln (leicht/schwer Angriff, Abwehr-Reduktion) —
      ergibt sich laut Absprache erst im direkten Spielfluss/Testing, nicht
      vorab am Reißbrett
- [ ] Exakte Champion-/Elite-Multiplikatoren (aktuell 1.5x/2.0x als
      Platzhalter)
- [ ] Upgrade-Kosten-Formel für Waffe/Rüstung
- [ ] Start-Equipment-Werte des Spielers
- [ ] Exakte Gewichtungswerte der Gegner-KI (`random.choices`-Weights)

## 7. Bewusst NICHT im Scope (mögliche spätere Erweiterung)

- Level-System für den Spieler
- Item-Loot / Inventarverwaltung über Basis-Equipment hinaus
- Sonderangriffe für Champion/Elite
- Grafische Oberfläche (geplant als separater Pygame-Nachbau)

## 8. Modul-Roadmap (Reihenfolge der Implementierung)

**Import-Konvention:** Jedes Package bekommt Re-Exports in seiner
`__init__.py`, sobald die enthaltenen Klassen existieren, z. B.:

```python
# character/__init__.py
from .base import Character
from .player import Player
from .enemy import Enemy
```

Dadurch sind Importe von außen kurz: `from character import Player, Enemy`
statt `from character.player import Player`. Wird pro Package direkt nach
dessen Implementierung ergänzt (siehe Reihenfolge unten).

1. `exceptions/custom_exceptions.py` — Basis-Exceptions zuerst, da andere
   Module sie nutzen
2. `character/base.py` — Character-Basisklasse
3. `character/player.py`, `character/enemy.py` — Vererbung
4. `items/equipment.py` — Waffe/Rüstung inkl. Upgrade-Logik
5. `world/enemy_data.py`, `world/biomes.py` — Datenbasis für Gegner/Biome
6. `combat/engine.py` — Rundenlogik, nutzt Character + Exceptions
7. `save/save_system.py` — JSON-Handling
8. `main.py` — alles zur Game-Loop zusammenführen

## 9. PCAP-Abdeckung durch dieses Projekt

Abgedeckt: OOP/Vererbung, Exceptions, Module, Dateihandling (JSON),
Kontrollfluss, Dictionaries/Listen.

Nicht abgedeckt (separat zu üben): Rekursion, `*args`/`**kwargs`,
`@classmethod`/`@staticmethod`, shallow vs. deep copy, Mehrfachvererbung/MRO,
Generatoren/Iteratoren.
