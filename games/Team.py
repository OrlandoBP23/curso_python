"""
 Class Team: Equipo
"""

from Athlete import Athlete
from Sport import Sport

class Team:
    """
    Clase para representar un equipo.
    """
    def __init__(self, name: str, sport: 'Sport', players: list):
        """
        Constructor de la clase Team.
        """
        self.name = name
        self.sport = sport
        self.players = players

    def __str__(self):
        return f"Team: {self.name}, {self.sport}, {self.players}"
    
    def __repr__(self):
        return f"Team:(name='{self.name}', sport={self.sport}, players={self.players})"

    def to_json(self)-> dict:
        return {"name":self.name, "sport":self.sport.to_json(), "players":[p.to_json() for p in self.players]}
    
if __name__ == "__main__":
    a1 = Athlete("Michel Jordan")
    a2 = Athlete("Scottie Pippen")
    a3 = Athlete("Kevin Durant")
    a4 = Athlete("Lebron James")
    a5 = Athlete("Nikola Jokic")
    s = Sport("Basketball", 5, "NBA")
    lakers = Team("Los Angeles Lakers", s, [a1,a2,a3,a4,a5])
    print(lakers)
    print(repr(lakers))



