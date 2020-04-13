from random import choice

from Buildings.farm import farm
from Buildings.flowers import flowers
from Buildings.fountain import fountain
from Buildings.house1 import house1
from Buildings.house2 import house2
from Buildings.library import library
from Buildings.mansion import mansion


class BuildingFactory:
    def __init__(self):
        self.buildings = {
            6: [flowers, fountain],
            8: [house1, house2],
            10: [library, farm],
            12: [mansion]
        }

    def choose_building(self, width):
        try:
            return choice(self.buildings[width])
        except:
            return None
