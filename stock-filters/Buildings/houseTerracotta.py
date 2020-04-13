from Buildings.material import AIR, LOG, PLANK, STAIRS, BED, DOOR, STONE, SAPLING, TERRACOTTA, WINDOW

temp = "placeholder"
selections = TERRACOTTA.values()

house_terracotta_template = [
    [
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, LOG, STONE, STONE, STONE, STONE, LOG, AIR],
        [AIR, STONE, PLANK, PLANK, PLANK, PLANK, STONE, AIR],
        [AIR, STONE, PLANK, PLANK, PLANK, PLANK, STONE, AIR],
        [AIR, STONE, PLANK, PLANK, PLANK, PLANK, STONE, AIR],
        [AIR, STONE, PLANK, PLANK, PLANK, PLANK, STONE, AIR],
        [AIR, LOG, STONE, STONE, STONE, STONE, LOG, AIR],
        [AIR, AIR, SAPLING, SAPLING, STAIRS["W"], STAIRS["W"], AIR, AIR]
    ],
    [
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, LOG, temp, temp, temp, temp, LOG, AIR],
        [AIR, temp, AIR, AIR, BED["S_FOOT"], BED["S_HEAD"], temp, AIR],
        [AIR, temp, AIR, AIR, AIR, AIR, temp, AIR],
        [AIR, temp, AIR, AIR, AIR, AIR, temp, AIR],
        [AIR, temp, AIR, AIR, AIR, AIR, temp, AIR],
        [AIR, LOG, temp, temp, DOOR["W_LOWER"], DOOR["S_LOWER"], LOG, AIR],
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
    ],
    [
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, LOG, temp, WINDOW, WINDOW, temp, LOG, AIR],
        [AIR, temp, AIR, AIR, AIR, AIR, temp, AIR],
        [AIR, WINDOW, AIR, AIR, AIR, AIR, WINDOW, AIR],
        [AIR, WINDOW, AIR, AIR, AIR, AIR, WINDOW, AIR],
        [AIR, temp, AIR, AIR, AIR, AIR, temp, AIR],
        [AIR, LOG, temp, temp, DOOR["RIGHT_UPPER"], DOOR["RIGHT_UPPER"], LOG, AIR],
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
    ],
    [
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, LOG, temp, temp, temp, temp, LOG, AIR],
        [AIR, temp, AIR, AIR, AIR, AIR, temp, AIR],
        [AIR, temp, AIR, AIR, AIR, AIR, temp, AIR],
        [AIR, temp, AIR, AIR, AIR, AIR, temp, AIR],
        [AIR, temp, AIR, AIR, AIR, AIR, temp, AIR],
        [AIR, LOG, temp, temp, temp, temp, LOG, AIR],
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
    ],
    [
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, LOG, temp, temp, temp, temp, LOG, AIR],
        [AIR, temp, AIR, AIR, AIR, AIR, temp, AIR],
        [AIR, temp, AIR, AIR, AIR, AIR, temp, AIR],
        [AIR, temp, AIR, AIR, AIR, AIR, temp, AIR],
        [AIR, temp, AIR, AIR, AIR, AIR, temp, AIR],
        [AIR, LOG, temp, temp, temp, temp, LOG, AIR],
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
    ],
    [
        [PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK],
        [PLANK, AIR, AIR, AIR, AIR, AIR, AIR, PLANK],
        [PLANK, AIR, AIR, AIR, AIR, AIR, AIR, PLANK],
        [PLANK, AIR, AIR, AIR, AIR, AIR, AIR, PLANK],
        [PLANK, AIR, AIR, AIR, AIR, AIR, AIR, PLANK],
        [PLANK, AIR, AIR, AIR, AIR, AIR, AIR, PLANK],
        [PLANK, AIR, AIR, AIR, AIR, AIR, AIR, PLANK],
        [PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK],
    ],
    [
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, AIR],
        [AIR, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, AIR],
        [AIR, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, AIR],
        [AIR, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, AIR],
        [AIR, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, AIR],
        [AIR, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, AIR],
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
    ],
    [
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, AIR, PLANK, PLANK, PLANK, PLANK, AIR, AIR],
        [AIR, AIR, PLANK, PLANK, PLANK, PLANK, AIR, AIR],
        [AIR, AIR, PLANK, PLANK, PLANK, PLANK, AIR, AIR],
        [AIR, AIR, PLANK, PLANK, PLANK, PLANK, AIR, AIR],
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
    ]
]


def generate_houses_terracotta():
    """This function will generate a list of houses made from different types of terracotta"""
    houses = []
    for selection in selections:
        new_house = []
        for floor in house_terracotta_template:
            new_floor = []
            for row in floor:
                new_row = []
                for item in row:
                    if item == temp:
                        new_row.append(selection)
                    else:
                        new_row.append(item)
                new_floor.append(new_row)
            new_house.append(new_floor)

        new_blueprint = {
            "height": 0,
            "building": new_house
        }
        houses.append(new_blueprint)
    return houses
