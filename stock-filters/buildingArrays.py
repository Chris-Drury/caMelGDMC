from random import choice

from Buildings.Width10 import farm, library
from Buildings.Width12 import mansion
from Buildings.Width6 import flowers, fountain
from Buildings.Width8 import house1, house2


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

