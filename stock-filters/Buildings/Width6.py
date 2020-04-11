from Buildings.Materials import AIR, GRASS, TRAPDOOR, WALL_SIGN, FLOWER, DIRT, BRICKS, WATER, FENCE, TORCH

flowers = {
    "height": -1,
    "building": [
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
            [AIR, TRAPDOOR["E"], GRASS, GRASS, WALL_SIGN, AIR],
            [AIR, TRAPDOOR["E"], GRASS, GRASS, TRAPDOOR["W"], AIR],
            [AIR, AIR, TRAPDOOR["N"], TRAPDOOR["N"], AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR],
        ],
        [
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, FLOWER["POPPY"], AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR],
        ]
    ]
}

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
