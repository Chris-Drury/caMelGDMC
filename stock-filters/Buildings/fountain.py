from Buildings.material import DIRT, BRICKS, WATER, AIR, FENCE, TORCH

fountain = {
    "height": -1,
    "building": [
        [
            [DIRT, DIRT, DIRT, DIRT, DIRT, DIRT],
            [DIRT, BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], DIRT],
            [DIRT, BRICKS["STONE"], WATER, WATER, BRICKS["STONE"], DIRT],
            [DIRT, BRICKS["STONE"], WATER, WATER, BRICKS["STONE"], DIRT],
            [DIRT, BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], DIRT],
            [DIRT, DIRT, DIRT, DIRT, DIRT, DIRT]
        ],
        [
            [BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"]],
            [BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"]],
            [BRICKS["STONE"], BRICKS["STONE"], WATER, WATER, BRICKS["STONE"], BRICKS["STONE"]],
            [BRICKS["STONE"], BRICKS["STONE"], WATER, WATER, BRICKS["STONE"], BRICKS["STONE"]],
            [BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"]],
            [BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"]]
        ],
        [
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], AIR],
            [AIR, BRICKS["STONE"], AIR, AIR, BRICKS["STONE"], AIR],
            [AIR, BRICKS["STONE"], AIR, AIR, BRICKS["STONE"], AIR],
            [AIR, BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, FENCE, AIR, AIR, FENCE, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, FENCE, AIR, AIR, FENCE, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, FENCE, AIR, AIR, FENCE, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, FENCE, AIR, AIR, FENCE, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], AIR],
            [AIR, BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], AIR],
            [AIR, BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], AIR],
            [AIR, BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, TORCH["UP"], AIR, AIR, TORCH["UP"], AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, TORCH["UP"], AIR, AIR, TORCH["UP"], AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR]
        ]
    ]
}


def generate_fountains():
    return [fountain]
