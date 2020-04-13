from random import choice

from Buildings.farm import generate_farms
from Buildings.flowers import generate_flowers
from Buildings.fountain import generate_fountains
from Buildings.houseBrick import generate_houses_brick
from Buildings.houseTerracotta import generate_houses_terracotta
from Buildings.library import generate_libraries
from Buildings.mansion import generate_mansions


class BuildingFactory:
    def __init__(self):
        self.buildings = {
            6: generate_fountains() + generate_flowers(),
            8: generate_houses_brick() + generate_houses_terracotta(),
            10: generate_libraries() + generate_farms(),
            12: generate_mansions()
        }

    def choose_building(self, width):
        try:
            return choice(self.buildings[width])
        except:
            return None
