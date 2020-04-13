from Buildings.material import LOG, AIR, STONE, STAIRS_COBBLESTONE, PLANK, BOOKSHELF, DOOR, STAIRS

library = {
    "height": 0,
    "building": [
        [
            [LOG, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, LOG],
            [STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE],
            [STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE],
            [STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE],
            [STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE],
            [STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE, STONE],
            [LOG, STONE, LOG, STONE, STONE, STONE, STONE, LOG, STONE, LOG],
            [AIR, AIR, AIR, STONE, STONE, STONE, STONE, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, STAIRS_COBBLESTONE["W"], STAIRS_COBBLESTONE["W"], AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
        ],
        [
            [LOG, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, LOG],
            [PLANK, BOOKSHELF, BOOKSHELF, BOOKSHELF, BOOKSHELF, BOOKSHELF, BOOKSHELF, BOOKSHELF, BOOKSHELF, PLANK],
            [PLANK, BOOKSHELF, AIR, AIR, AIR, AIR, AIR, AIR, BOOKSHELF, PLANK],
            [PLANK, BOOKSHELF, AIR, AIR, AIR, AIR, AIR, AIR, BOOKSHELF, PLANK],
            [PLANK, BOOKSHELF, AIR, AIR, AIR, AIR, AIR, AIR, BOOKSHELF, PLANK],
            [PLANK, BOOKSHELF, AIR, AIR, AIR, AIR, AIR, AIR, BOOKSHELF, PLANK],
            [LOG, PLANK, LOG, AIR, AIR, AIR, AIR, LOG, PLANK, LOG],

            [AIR, AIR, AIR, PLANK, DOOR["E_LOWER"], DOOR["E_LOWER"], PLANK, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [LOG, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, LOG],
            [PLANK, BOOKSHELF, BOOKSHELF, BOOKSHELF, BOOKSHELF, BOOKSHELF, BOOKSHELF, BOOKSHELF, BOOKSHELF, PLANK],
            [PLANK, BOOKSHELF, AIR, AIR, AIR, AIR, AIR, AIR, BOOKSHELF, PLANK],
            [PLANK, BOOKSHELF, AIR, AIR, AIR, AIR, AIR, AIR, BOOKSHELF, PLANK],
            [PLANK, BOOKSHELF, AIR, AIR, AIR, AIR, AIR, AIR, BOOKSHELF, PLANK],
            [PLANK, BOOKSHELF, AIR, AIR, AIR, AIR, AIR, AIR, BOOKSHELF, PLANK],
            [LOG, PLANK, LOG, AIR, AIR, AIR, AIR, LOG, PLANK, LOG],

            [AIR, AIR, AIR, PLANK, DOOR["LEFT_UPPER"], DOOR["RIGHT_UPPER"], PLANK, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [LOG, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, LOG],
            [PLANK, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, PLANK],
            [PLANK, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, PLANK],
            [PLANK, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, PLANK],
            [PLANK, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, PLANK],
            [PLANK, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, PLANK],
            [LOG, PLANK, LOG, AIR, AIR, AIR, AIR, LOG, PLANK, LOG],

            [AIR, AIR, AIR, PLANK, PLANK, PLANK, PLANK, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [LOG, LOG, LOG, LOG, LOG, LOG, LOG, LOG, LOG, LOG],
            [LOG, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, LOG],
            [LOG, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, LOG],
            [LOG, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, LOG],
            [LOG, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, LOG],
            [LOG, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, LOG],
            [LOG, LOG, LOG, LOG, LOG, LOG, LOG, LOG, LOG, LOG],

            [AIR, AIR, AIR, LOG, LOG, LOG, LOG, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [STAIRS["S"], PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, STAIRS["N"]],
            [STAIRS["S"], AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, STAIRS["N"]],
            [STAIRS["S"], AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, STAIRS["N"]],
            [STAIRS["S"], AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, STAIRS["N"]],
            [STAIRS["S"], AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, STAIRS["N"]],
            [STAIRS["S"], AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, STAIRS["N"]],
            [STAIRS["S"], PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, STAIRS["N"]],

            [AIR, AIR, AIR, STAIRS["S"], PLANK, PLANK, STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, STAIRS["S"], PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, STAIRS["N"], AIR],
            [AIR, STAIRS["S"], AIR, AIR, AIR, AIR, AIR, AIR, STAIRS["N"], AIR],
            [AIR, STAIRS["S"], AIR, AIR, AIR, AIR, AIR, AIR, STAIRS["N"], AIR],
            [AIR, STAIRS["S"], AIR, AIR, AIR, AIR, AIR, AIR, STAIRS["N"], AIR],
            [AIR, STAIRS["S"], AIR, AIR, AIR, AIR, AIR, AIR, STAIRS["N"], AIR],
            [AIR, STAIRS["S"], AIR, AIR, AIR, AIR, AIR, AIR, STAIRS["N"], AIR],
            [AIR, STAIRS["S"], PLANK, PLANK, PLANK, PLANK, PLANK, PLANK, STAIRS["N"], AIR],

            [AIR, AIR, AIR, AIR, STAIRS["S"], STAIRS["N"], AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, AIR, STAIRS["S"], PLANK, PLANK, PLANK, PLANK, STAIRS["N"], AIR, AIR],
            [AIR, AIR, STAIRS["S"], AIR, AIR, AIR, AIR, STAIRS["N"], AIR, AIR],
            [AIR, AIR, STAIRS["S"], AIR, AIR, AIR, AIR, STAIRS["N"], AIR, AIR],
            [AIR, AIR, STAIRS["S"], AIR, AIR, AIR, AIR, STAIRS["N"], AIR, AIR],
            [AIR, AIR, STAIRS["S"], AIR, AIR, AIR, AIR, STAIRS["N"], AIR, AIR],
            [AIR, AIR, STAIRS["S"], AIR, AIR, AIR, AIR, STAIRS["N"], AIR, AIR],
            [AIR, AIR, STAIRS["S"], PLANK, PLANK, PLANK, PLANK, STAIRS["N"], AIR, AIR],

            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ],
        [
            [AIR, AIR, AIR, STAIRS["S"], PLANK, PLANK, STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, STAIRS["S"], PLANK, PLANK, STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, STAIRS["S"], PLANK, PLANK, STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, STAIRS["S"], PLANK, PLANK, STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, STAIRS["S"], PLANK, PLANK, STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, STAIRS["S"], PLANK, PLANK, STAIRS["N"], AIR, AIR, AIR],
            [AIR, AIR, AIR, STAIRS["S"], PLANK, PLANK, STAIRS["N"], AIR, AIR, AIR],

            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR],
            [AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR, AIR]
        ]
    ]
}


def generate_libraries():
    return [library]
