from Buildings.material import AIR, LOG, PLANK, STAIRS, BED, DOOR, STONE, SAPLING, TERRACOTTA, WINDOW

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

# def get_coloured_houses():
#     houses = []
#     for color in terracotta.values:

