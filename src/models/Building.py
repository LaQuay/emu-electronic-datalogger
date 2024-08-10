from typing import List

from src.models.Consumption import MonthlyVolume


class Flat:
    id: int
    label: str
    serial: int
    consumption: List[MonthlyVolume]

    def __init__(self, id, label, serial):
        self.id = id
        self.label = label
        self.serial = serial
        self.consumption = []


class Building:
    flats: List[Flat]

    def __init__(self):
        self.flats = []
