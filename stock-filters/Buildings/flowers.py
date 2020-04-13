from Buildings.material import AIR, GRASS, TRAPDOOR, WALL_SIGN, FLOWER

temp = "placeholder"
selections = FLOWER.values()

flowers_template = [
    [
        [AIR, GRASS, GRASS, GRASS, AIR, GRASS],
        [AIR, AIR, GRASS, GRASS, GRASS, GRASS],
        [GRASS, GRASS, GRASS, GRASS, GRASS, AIR],
        [GRASS, GRASS, GRASS, GRASS, AIR, GRASS],
        [GRASS, GRASS, GRASS, GRASS, GRASS, AIR],
        [AIR, GRASS, AIR, GRASS, GRASS, GRASS],
    ],
    [
        [AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, AIR, TRAPDOOR["S"], TRAPDOOR["S"], AIR, AIR],
        [AIR, TRAPDOOR["E"], GRASS, GRASS, TRAPDOOR["W"], AIR],
        [AIR, TRAPDOOR["E"], GRASS, GRASS, TRAPDOOR["W"], AIR],
        [AIR, AIR, TRAPDOOR["N"], TRAPDOOR["N"], AIR, AIR],
        [AIR, AIR, AIR, AIR, AIR, AIR],
    ],
    [
        [AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, AIR, temp, temp, AIR, AIR],
        [AIR, AIR, temp, temp, AIR, AIR],
        [AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, AIR, AIR, AIR, AIR, AIR],
    ]
]


def generate_flowers():
    """This function will generate a list of flower plots made from different types of flowers"""
    flowers = []
    for selection in selections:
        new_flower = []
        for floor in flowers_template:
            new_floor = []
            for row in floor:
                new_row = []
                for item in row:
                    if item == temp:
                        new_row.append(selection)
                    else:
                        new_row.append(item)
                new_floor.append(new_row)
            new_flower.append(new_floor)

        new_blueprint = {
            "height": -1,
            "building": new_flower
        }
        flowers.append(new_blueprint)
    return flowers
