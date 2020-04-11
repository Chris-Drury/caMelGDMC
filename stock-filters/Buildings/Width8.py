from Buildings.Materials import AIR, LOG, BRICKS, PLANK, STAIRS_STONE, STAIRS, BED, DOOR, WOOD, GLASS, TORCH, STONE, \
    SAPLING, TERRACOTTA, WINDOW

house1 = {
    "height": 0,
    "building": [
        [
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, LOG, BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], LOG, AIR],
            [AIR, BRICKS["STONE"], LOG, PLANK, PLANK, LOG, BRICKS["STONE"], AIR],
            [AIR, BRICKS["STONE"], PLANK, PLANK, PLANK, PLANK, BRICKS["STONE"], AIR],
            [AIR, BRICKS["STONE"], LOG, PLANK, PLANK, LOG, BRICKS["STONE"], AIR],
            [AIR, LOG, BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], LOG, AIR],
            [AIR, AIR, STAIRS_STONE["W"], STAIRS_STONE["W"], STAIRS_STONE["W"], STAIRS_STONE["W"], AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, LOG, BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], LOG, AIR],
            [AIR, BRICKS["STONE"], STAIRS["N"], AIR, AIR, AIR, BRICKS["STONE"], AIR],
            [AIR, BRICKS["STONE"], BED["W_HEAD_TAKEN"], AIR, AIR, AIR, BRICKS["STONE"], AIR],
            [AIR, BRICKS["STONE"], BED["W_FOOT"], AIR, AIR, AIR, BRICKS["STONE"], AIR],
            [AIR, LOG, BRICKS["STONE"], DOOR["W_LOWER"], DOOR["S_LOWER"], BRICKS["STONE"], LOG, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, LOG, WOOD["STRIPPED_OAK"], GLASS, GLASS, WOOD["STRIPPED_OAK"], LOG, AIR],
            [AIR, WOOD["ACACIA"], AIR, AIR, AIR, AIR, WOOD["ACACIA"], AIR],
            [AIR, GLASS, AIR, AIR, AIR, AIR, GLASS, AIR],
            [AIR, WOOD["ACACIA"], AIR, AIR, AIR, AIR, WOOD["ACACIA"], AIR],
            [AIR, LOG, WOOD["STRIPPED_OAK"], DOOR["LEFT_UPPER"], DOOR["LEFT_UPPER"], WOOD["STRIPPED_OAK"], LOG, AIR],
            [AIR, AIR, TORCH["E"], AIR, AIR, TORCH["E"], AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [STAIRS["S"], STAIRS["N_FLIPPED"], AIR, AIR, AIR, AIR, STAIRS["S_FLIPPED"], STAIRS["N"]],
            [STAIRS["S"], LOG, BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], LOG, STAIRS["N"]],
            [STAIRS["S"], BRICKS["STONE"], AIR, AIR, AIR, AIR, BRICKS["STONE"], STAIRS["N"]],
            [STAIRS["S"], BRICKS["STONE"], AIR, AIR, AIR, AIR, BRICKS["STONE"], STAIRS["N"]],
            [STAIRS["S"], BRICKS["STONE"], AIR, TORCH["W"], TORCH["W"], AIR, BRICKS["STONE"], STAIRS["N"]],
            [STAIRS["S"], LOG, BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], LOG, STAIRS["N"]],
            [STAIRS["S"], STAIRS["N_FLIPPED"], AIR, AIR, AIR, AIR, STAIRS["S_FLIPPED"], STAIRS["N"]],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, STAIRS["S"], STAIRS["N_FLIPPED"], AIR, AIR, STAIRS["S_FLIPPED"], STAIRS["N"], AIR],
            [AIR, STAIRS["S"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], STAIRS["N"], AIR],
            [AIR, STAIRS["S"], AIR, AIR, AIR, AIR, STAIRS["N"], AIR],
            [AIR, STAIRS["S"], AIR, AIR, AIR, AIR, STAIRS["N"], AIR],
            [AIR, STAIRS["S"], AIR, AIR, AIR, AIR, STAIRS["N"], AIR],
            [AIR, STAIRS["S"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], BRICKS["STONE"], STAIRS["N"], AIR],
            [AIR, STAIRS["S"], STAIRS["N_FLIPPED"], AIR, AIR, STAIRS["S_FLIPPED"], STAIRS["N"], AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, AIR, STAIRS["S"], STAIRS["N_FLIPPED"], STAIRS["S_FLIPPED"], STAIRS["N"], AIR, AIR],
            [AIR, AIR, STAIRS["S"], BRICKS["STONE"], BRICKS["STONE"], STAIRS["N"], AIR, AIR],
            [AIR, AIR, STAIRS["S"], AIR, AIR, STAIRS["N"], AIR, AIR],
            [AIR, AIR, STAIRS["S"], AIR, AIR, STAIRS["N"], AIR, AIR],
            [AIR, AIR, STAIRS["S"], AIR, AIR, STAIRS["N"], AIR, AIR],
            [AIR, AIR, STAIRS["S"], BRICKS["STONE"], BRICKS["STONE"], STAIRS["N"], AIR, AIR],
            [AIR, AIR, STAIRS["S"], STAIRS["N_FLIPPED"], STAIRS["S_FLIPPED"], STAIRS["N"], AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, AIR, AIR, STAIRS["S"], STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, STAIRS["S"], STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, STAIRS["S"], STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, STAIRS["S"], STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, STAIRS["S"], STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, STAIRS["S"], STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, STAIRS["S"], STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ]
    ]
}

house2 = {
    "height": 0,
    "building": [
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
            [AIR, LOG, TERRACOTTA, TERRACOTTA, TERRACOTTA, TERRACOTTA, LOG, AIR],
            [AIR, TERRACOTTA, AIR, AIR, BED["S_FOOT"], BED["S_HEAD"], TERRACOTTA, AIR],
            [AIR, TERRACOTTA, AIR, AIR, AIR, AIR, TERRACOTTA, AIR],
            [AIR, TERRACOTTA, AIR, AIR, AIR, AIR, TERRACOTTA, AIR],
            [AIR, TERRACOTTA, AIR, AIR, AIR, AIR, TERRACOTTA, AIR],
            [AIR, LOG, TERRACOTTA, TERRACOTTA, DOOR["W_LOWER"], DOOR["S_LOWER"], LOG, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, LOG, TERRACOTTA, WINDOW, WINDOW, TERRACOTTA, LOG, AIR],
            [AIR, TERRACOTTA, AIR, AIR, AIR, AIR, TERRACOTTA, AIR],
            [AIR, WINDOW, AIR, AIR, AIR, AIR, WINDOW, AIR],
            [AIR, WINDOW, AIR, AIR, AIR, AIR, WINDOW, AIR],
            [AIR, TERRACOTTA, AIR, AIR, AIR, AIR, TERRACOTTA, AIR],
            [AIR, LOG, TERRACOTTA, TERRACOTTA, DOOR["RIGHT_UPPER"], DOOR["RIGHT_UPPER"], LOG, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, LOG, TERRACOTTA, TERRACOTTA, TERRACOTTA, TERRACOTTA, LOG, AIR],
            [AIR, TERRACOTTA, AIR, AIR, AIR, AIR, TERRACOTTA, AIR],
            [AIR, TERRACOTTA, AIR, AIR, AIR, AIR, TERRACOTTA, AIR],
            [AIR, TERRACOTTA, AIR, AIR, AIR, AIR, TERRACOTTA, AIR],
            [AIR, TERRACOTTA, AIR, AIR, AIR, AIR, TERRACOTTA, AIR],
            [AIR, LOG, TERRACOTTA, TERRACOTTA, TERRACOTTA, TERRACOTTA, LOG, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, LOG, TERRACOTTA, TERRACOTTA, TERRACOTTA, TERRACOTTA, LOG, AIR],
            [AIR, TERRACOTTA, AIR, AIR, AIR, AIR, TERRACOTTA, AIR],
            [AIR, TERRACOTTA, AIR, AIR, AIR, AIR, TERRACOTTA, AIR],
            [AIR, TERRACOTTA, AIR, AIR, AIR, AIR, TERRACOTTA, AIR],
            [AIR, TERRACOTTA, AIR, AIR, AIR, AIR, TERRACOTTA, AIR],
            [AIR, LOG, TERRACOTTA, TERRACOTTA, TERRACOTTA, TERRACOTTA, LOG, AIR],
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
}
