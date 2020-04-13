from Buildings.material import AIR, GRASS, TRAPDOOR, WALL_SIGN, FLOWER

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

