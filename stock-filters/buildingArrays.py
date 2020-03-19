from random import choice

Demo8x8x7_pink = [[
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "17:0", "4:0", "4:0", "4:0", "4:0", "17:0", "0:0"],
    ["0:0", "4:0", "17:0", "5:0", "5:0", "17:0", "4:0", "0:0"],
    ["0:0", "4:0", "5:0", "5:0", "5:0", "5:0", "4:0", "0:0"],
    ["0:0", "4:0", "17:0", "5:0", "5:0", "17:0", "4:0", "0:0"],
    ["0:0", "17:0", "4:0", "4:0", "4:0", "4:0", "17:0", "0:0"],
    ["0:0", "0:0", "67:1", "67:1", "67:1", "67:1", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "17:0", "4:0", "4:0", "4:0", "4:0", "17:0", "0:0"],
    ["0:0", "4:0", "53:3", "0:0", "0:0", "0:0", "4:0", "0:0"],
    ["0:0", "4:0", "0:0", "0:0", "0:0", "0:0", "4:0", "0:0"],
    ["0:0", "4:0", "0:0", "0:0", "0:0", "0:0", "4:0", "0:0"],
    ["0:0", "17:0", "4:0", "64:0", "64:0", "4:0", "17:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
]]

Demo8x8x7 = [[
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "17:0", "4:0", "4:0", "4:0", "4:0", "17:0", "0:0"],
    ["0:0", "4:0", "17:0", "5:0", "5:0", "17:0", "4:0", "0:0"],
    ["0:0", "4:0", "5:0", "5:0", "5:0", "5:0", "4:0", "0:0"],
    ["0:0", "4:0", "17:0", "5:0", "5:0", "17:0", "4:0", "0:0"],
    ["0:0", "17:0", "4:0", "4:0", "4:0", "4:0", "17:0", "0:0"],
    ["0:0", "0:0", "67:1", "67:1", "67:1", "67:1", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "17:0", "4:0", "4:0", "4:0", "4:0", "17:0", "0:0"],
    ["0:0", "4:0", "53:3", "0:0", "0:0", "0:0", "4:0", "0:0"],
    ["0:0", "4:0", "0:0", "0:0", "0:0", "0:0", "4:0", "0:0"],
    ["0:0", "4:0", "0:0", "0:0", "0:0", "0:0", "4:0", "0:0"],
    ["0:0", "17:0", "4:0", "64:1", "64:2", "4:0", "17:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "17:0", "17:8", "102:0", "102:0", "17:8", "17:0", "0:0"],
    ["0:0", "17:4", "0:0", "0:0", "0:0", "0:0", "17:4", "0:0"],
    ["0:0", "102:0", "0:0", "0:0", "0:0", "0:0", "102:0", "0:0"],
    ["0:0", "17:4", "0:0", "0:0", "0:0", "0:0", "17:4", "0:0"],
    ["0:0", "17:0", "17:8", "64:8", "64:8", "17:8", "17:0", "0:0"],
    ["0:0", "0:0", "50:1", "0:0", "0:0", "50:1", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    ["53:2", "53:11", "0:0", "0:0", "0:0", "0:0", "53:10", "53:3"],
    ["53:2", "17:0", "4:0", "4:0", "4:0", "4:0", "17:0", "53:3"],
    ["53:2", "4:0", "0:0", "0:0", "0:0", "0:0", "4:0", "53:3"],
    ["53:2", "4:0", "0:0", "0:0", "0:0", "0:0", "4:0", "53:3"],
    ["53:2", "4:0", "0:0", "50:2", "50:2", "0:0", "4:0", "53:3"],
    ["53:2", "17:0", "4:0", "4:0", "4:0", "4:0", "17:0", "53:3"],
    ["53:2", "53:11", "0:0", "0:0", "0:0", "0:0", "53:10", "53:3"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    ["0:0", "53:2", "53:11", "0:0", "0:0", "53:10", "53:3", "0:0"],
    ["0:0", "53:2", "4:0", "4:0", "4:0", "4:0", "53:3", "0:0"],
    ["0:0", "53:2", "0:0", "0:0", "0:0", "0:0", "53:3", "0:0"],
    ["0:0", "53:2", "0:0", "0:0", "0:0", "0:0", "53:3", "0:0"],
    ["0:0", "53:2", "0:0", "0:0", "0:0", "0:0", "53:3", "0:0"],
    ["0:0", "53:2", "4:0", "4:0", "4:0", "4:0", "53:3", "0:0"],
    ["0:0", "53:2", "53:11", "0:0", "0:0", "53:10", "53:3", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    ["0:0", "0:0", "53:2", "53:11", "53:10", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "53:2", "4:0", "4:0", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "53:2", "0:0", "0:0", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "53:2", "0:0", "0:0", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "53:2", "0:0", "0:0", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "53:2", "4:0", "4:0", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "53:2", "53:11", "53:10", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
]]


class BuildingFactory():
    def __init__(self):
        self.buildings = {
            8 : [Demo8x8x7, Demo8x8x7_pink]
        }

    def choose_building(self, width):
        try:
            return choice(self.buildings[width])
        except:
            return None
