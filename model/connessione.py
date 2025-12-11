from dataclasses import dataclass

@dataclass
class Connessione():
    id_rifugio1: int
    id_rifugio2: int
    difficolta: float
    distanza: float
    anno: int

    def __str__(self):
        return f"{self.id_rifugio1} -- {self.id_rifugio2} ({self.anno})"

    def __eq__(self, other):
        return isinstance(other, Connessione) and self.id_rifugio1 == other.id_rifugio1 and self.id_rifugio2 == other.id_rifugio2