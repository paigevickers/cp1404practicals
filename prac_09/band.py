"""Band class for CP1404"""


class Band:
    """Band class"""
    def __init__(self, name=""):
        """Initialise Band object"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """String representation of Band object"""
        return f"{self.name} ({self.musicians}"

    def add(self, musician):
        """Add musician to list of musicians"""
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            if not musician.instruments:
                return f"{musician.name} needs an instrument!"
            return f"{musician.name} is playing: {musician.instruments[0]}"