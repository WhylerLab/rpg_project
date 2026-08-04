# exceptions/custom_exceptions.py

class RPGError(Exception):
    """Basisklasse für alle spielspezifischen Fehler."""    # (""" Sind Docstrings """ Zeilenumbrüche müssen nicht manuel Escaped werden)
    pass


class InvalidActionError(RPGError):
    """Wird ausgelöst, wenn eine ungültige Kampfaktion gewählt wird."""     #print(InvalidActionError.__doc__)
    pass


class HealLimitReachedError(RPGError):
    """Wird ausgelöst, wenn Heilung öfter als erlaubt genutzt wird."""
    pass


class InsufficientGoldError(RPGError):
    """Wird ausgelöst, wenn Gold für ein Equipment-Upgrade nicht reicht."""
    pass


class MaxUpgradeReachedError(RPGError):
    """Wird ausgelöst, wenn Waffe/Rüstung bereits Stufe +5 erreicht hat."""
    pass


class SaveFileError(RPGError):
    """Wird ausgelöst bei Problemen beim Laden/Speichern der JSON-Datei."""
    pass