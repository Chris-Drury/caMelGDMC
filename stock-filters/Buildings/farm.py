from Buildings.material import LOG, FARMLAND, WATER, AIR, CARROTS, WHEAT, POTATOES

temp0 = "placeholder0"
temp1 = "placeholder1"
temp2 = "placeholder2"

selections = [
    [CARROTS, WHEAT, POTATOES],
    [CARROTS, POTATOES, WHEAT],
    [WHEAT, POTATOES, CARROTS],
    [WHEAT, CARROTS, POTATOES],
    [POTATOES, CARROTS, WHEAT],
    [POTATOES, WHEAT, CARROTS]
]

farm_template = [
    [
        [LOG, LOG, LOG, LOG, LOG, LOG, LOG, LOG, LOG, LOG],
        [LOG, FARMLAND, WATER, FARMLAND, FARMLAND, FARMLAND, FARMLAND, WATER, FARMLAND, LOG],
        [LOG, FARMLAND, WATER, FARMLAND, FARMLAND, FARMLAND, FARMLAND, WATER, FARMLAND, LOG],
        [LOG, FARMLAND, WATER, FARMLAND, FARMLAND, FARMLAND, FARMLAND, WATER, FARMLAND, LOG],
        [LOG, FARMLAND, WATER, FARMLAND, FARMLAND, FARMLAND, FARMLAND, WATER, FARMLAND, LOG],
        [LOG, FARMLAND, WATER, FARMLAND, FARMLAND, FARMLAND, FARMLAND, WATER, FARMLAND, LOG],
        [LOG, FARMLAND, WATER, FARMLAND, FARMLAND, FARMLAND, FARMLAND, WATER, FARMLAND, LOG],
        [LOG, FARMLAND, WATER, FARMLAND, FARMLAND, FARMLAND, FARMLAND, WATER, FARMLAND, LOG],
        [LOG, FARMLAND, WATER, FARMLAND, FARMLAND, FARMLAND, FARMLAND, WATER, FARMLAND, LOG],
        [LOG, LOG, LOG, LOG, LOG, LOG, LOG, LOG, LOG, LOG],
    ],
    [
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
        [AIR, temp0, AIR, temp1, temp1, temp1, temp1, AIR, temp2, AIR],
        [AIR, temp0, AIR, temp1, temp1, temp1, temp1, AIR, temp2, AIR],
        [AIR, temp0, AIR, temp1, temp1, temp1, temp1, AIR, temp2, AIR],
        [AIR, temp0, AIR, temp1, temp1, temp1, temp1, AIR, temp2, AIR],
        [AIR, temp0, AIR, temp1, temp1, temp1, temp1, AIR, temp2, AIR],
        [AIR, temp0, AIR, temp1, temp1, temp1, temp1, AIR, temp2, AIR],
        [AIR, temp0, AIR, temp1, temp1, temp1, temp1, AIR, temp2, AIR],
        [AIR, temp0, AIR, temp1, temp1, temp1, temp1, AIR, temp2, AIR],
        [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
    ]
]


def generate_farms():
    """This function will generate a list of farms that contain every possible combination of items"""
    farms = []
    for selection in selections:
        new_farm = []
        for floor in farm_template:
            new_floor = []
            for row in floor:
                new_row = []
                for item in row:
                    if item == temp0:
                        new_row.append(selection[0])
                    elif item == temp1:
                        new_row.append(selection[1])
                    elif item == temp2:
                        new_row.append(selection[2])
                    else:
                        new_row.append(item)
                new_floor.append(new_row)
            new_farm.append(new_floor)

        new_blueprint = {
            "height": -1,
            "building": new_farm
        }
        farms.append(new_blueprint)
    return farms

