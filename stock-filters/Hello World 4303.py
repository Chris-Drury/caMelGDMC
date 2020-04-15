from random import randint
from buildingArrays import BuildingFactory
import utilityFunctions

#inputs are taken from the user. Here I've just showing labels, as well as letting the user define
# what the main creation material for the structures is
inputs = (
	("COMP4303 Final Project", "label"),
	("caMel", "label"),
	)

foliage = [6, 17, 18, 31, 32, 37, 38, 39, 40, 81, 83, 86, 99, 100, 103, 111, 127, 161, 162, 175]
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # right, up, left, down
lastDirectionInt = 5 # lets use this so it can never back track...
buildingLocations = [] # lets define a list of all locations that will need buildings
woodTypePerBiome = {    # biome: tree data
    4: 2,               # forest: birch
    5: 1,               # taiga: spruce
    12: 1,              # snowy tundra: spruce
    13: 1,              # snowy mountains: spruce
    19: 1,              # taiga hills: spruce
    21: 3,              # jungle: jungle
    22: 3,              # jungle hills: jungle
    23: 3,              # jungle edge: jungle
    27: 2,              # birch forest: birch
    28: 2,              # birch forest hills: birch
    30: 1,              # snowy taiga: spruce
    31: 1,              # snowy taiga hills: spruce
    32: 1,              # mega taiga: spruce
    133: 1,             # taiga mountains: spruce
    149: 3,             # modified jungle: jungle
    151: 3,             # modified jungle edge: jungle
    155: 2,             # tall birch forest: birch
    156: 2,             # tall birch hills: birch
    158: 1,             # snowy taiga mountains: spruce
    168: 3,             # bamboo jungle: jungle
    169: 3,             # bamboo jungle hills: jungle
}
stairBlockTypePerBiome = {
    4: 135,             # forest: birch
    5: 134,             # taiga: spruce
    12: 134,            # snowy tundra: spruce
    13: 134,            # snowy mountains: spruce
    19: 134,            # taiga hills: spruce
    21: 136,            # jungle: jungle
    22: 136,            # jungle hills: jungle
    23: 136,            # jungle edge: jungle
    27: 135,            # birch forest: birch
    28: 135,            # birch forest hills: birch
    30: 134,            # snowy taiga: spruce
    31: 134,            # snowy taiga hills: spruce
    32: 134,            # mega taiga: spruce
    133: 134,           # taiga mountains: spruce
    149: 136,           # modified jungle: jungle
    151: 136,           # modified jungle edge: jungle
    155: 135,           # tall birch forest: birch
    156: 135,           # tall birch hills: birch
    158: 134,           # snowy taiga mountains: spruce
    168: 136,           # bamboo jungle: jungle
    169: 136,           # bamboo jungle hills: jungle
}

maxx = None; maxy = None; maxz = None; minx = None; miny = None; minz = None

# The required method for MCEdit. This function will be what runs the filter.
def perform(level, box, options):
    global maxx, maxy, maxz, minx, miny, minz
    filterOptions = options
    maxx = box.maxx; maxy = box.maxy; maxz = box.maxz
    minx = box.minx; miny = box.miny; minz = box.minz
    # Build a 2D planning grid
    levelGrid = [[[0,0] for j in range(0, maxz - minz)] for i in range(minx, maxx)]

    # for step in xrange(0,4):
    print("Generating town layout...")
    generateLayout(level, levelGrid)

    # normalize the layout
    print("Smoothing out house plots...")
    normalizeBuildingLayout(level, box, levelGrid)

    # smooth out the terrain around plots
    print("smoothing out the terrain...")
    levelTerrain(level, levelGrid)

    # Place the grid on the terrain
    print("Generating terrain...")
    overlayGrid(levelGrid, level)

    # build houses
    print("Generating buildings...")
    bulidBuildings(level, minx, minz)

    print("Done!")

# Apply the levelGrid to the terrain
def overlayGrid(levelGrid, level):
    global minx, minz
    xLoc = minx

    for x in levelGrid:
        zLoc = minz
        for y in x:
            layoutType = y[0]
            height = y[1]
            wood = ["5","0"]

            if layoutType == 1:
                # house plots
                if ((level.blockAt(xLoc, height, zLoc) == 9) or (level.blockAt(xLoc, height, zLoc) == 8)):
                    block_data = modifyWoodToSuitBiome(wood, level.biomeAt(xLoc, zLoc))
                else:
                    block_data = (level.blockAt(xLoc, getHeight(level, xLoc, zLoc), zLoc), 0)

                utilityFunctions.setBlock(level, block_data, xLoc, height, zLoc)
            elif layoutType == 2:
                # paths
                height = getHeight(level, xLoc, zLoc, False)
                if ((level.blockAt(xLoc, height, zLoc) == 9) or (level.blockAt(xLoc, height, zLoc) == 8)):
                    block_data = modifyWoodToSuitBiome(wood, level.biomeAt(xLoc, zLoc))
                else:
                    block_data = (208, 0)

                utilityFunctions.setBlock(level, tuple(block_data), xLoc, height, zLoc)
            zLoc += 1
        xLoc += 1


def partitionList(array, startIndex, endIndex):
    pivot = array[endIndex]
    i = startIndex
    for j in range(startIndex, endIndex):
        if array[j][3] < pivot[3]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[endIndex] = array[endIndex], array[i]
    return i


def sortBuildingLocations(array, startIndex, endIndex):
    if startIndex < endIndex:
        point = partitionList(array, startIndex, endIndex)
        sortBuildingLocations(array, startIndex, point - 1)
        sortBuildingLocations(array, point + 1, endIndex)


# This will level out all building plots
def normalizeBuildingLayout(level, box, levelGrid):
    global minx, minz
    for location in buildingLocations:
        xDest = location[0]
        zDest = location[1]
        width = location[2] / 2

        heights = []
        # Gather heights
        for x in range(xDest - width, xDest + width):
            for z in range(zDest - width, zDest + width):
                heights.append(levelGrid[x][z][1])

        med = heights[int(len(heights) / 2)]
        location[3] = med

        # sort buildingLocation by median height
        sortBuildingLocations(buildingLocations, 0, len(buildingLocations) - 1)
        buildingLocations.reverse()

# This will create the layout on a 2D grid. The layout consists of house plots and roads/paths between each plot
def generateLayout(level, levelGrid):
    xSize = len(levelGrid)
    zSize = len(levelGrid[0])

    # create the first house. For now, always place it in the middle of the plot
    xEnd = xSize / 2
    zEnd = zSize / 2
    generateHousePlot(level, levelGrid, xEnd, zEnd, 3)

    # begin branching a creating the rest of the village
    for houses in range(0,40):
        # Generate a path of a random length in a random direction
        xEnd, zEnd = generatePath(level, levelGrid, xEnd, zEnd, randint(8, 40),  randint(0, 3))

        # Create the width of the next house plot and check that it will fit in the boundingBox
        plotWidth = randint(6,12) / 2
            # TODO: Ideally, this would be replaced by a function call that would check
        if (xEnd + plotWidth > xSize) or (xEnd - plotWidth < 0):
            continue
        elif (zEnd + plotWidth > zSize) or (zEnd - plotWidth < 0):
            continue
        elif checkHousePlot(levelGrid, xEnd, zEnd, plotWidth):
            generateHousePlot(level, levelGrid, xEnd, zEnd, plotWidth)

# This will generate the house plot
def generateHousePlot(level, levelGrid, xDest, zDest, width):
    global minx, minz
    buildingLocations.append([xDest, zDest, width * 2, 0])
    for x in xrange(xDest - width, xDest + width):
        for z in xrange(zDest - width, zDest + width):
            levelGrid[x][z] = [1, getHeight(level, minx + x, minz + z)]

# check that the house's plot will not override another plot
def checkHousePlot(levelGrid, xDest, zDest, width):
    for x in xrange(xDest - width, xDest + width):
        for z in xrange(zDest - width, zDest + width):
            if levelGrid[x][z][0] == 1:
                return False

    return True

# Get the hight of the terrain for a given X and Z
def getHeight(level, x, z, house_plot=True):
    global maxy, miny, foliage
    for y in xrange(maxy, miny, -1):
        blockID = level.blockAt(x, y, z)
        if blockID not in ([0] + foliage):
            if not house_plot:
                utilityFunctions.setBlock(level, (0, 0), x, y+1, z)
            return y
        elif blockID in foliage and house_plot:
            utilityFunctions.setBlock(level, (0, 0), x, y, z)

    return 0

# This will generate the paths, starting from the center of each house plot
def generatePath(level, levelGrid, xStart, zStart, pathLength, directionInt):
    global directions
    global lastDirectionInt

    # determine the direction for each path
    direction = directions[directionInt]
    xDir = direction[0]
    zDir = direction[1]

    i = 0
        #TODO: place this check in its own method
    while (xStart + xDir*pathLength > len(levelGrid)) or (xStart - xDir*pathLength < 0 ) or \
          (zStart + zDir*pathLength > len(levelGrid[0])) or (zStart - zDir*pathLength < 0 ) or \
          ((lastDirectionInt != directionInt) and ((lastDirectionInt - directionInt) % 4 == 0 or (lastDirectionInt - directionInt) % 4 == 2)):

        if (i == 10):
            # this check exists to make sure that the algorith does not spend too much time finding a suitable direction
            xStart, zStart = generatePath(level, levelGrid, len(levelGrid) / 2, len(levelGrid[0]) / 2, pathLength, directionInt)
            return xStart, zStart
        directionInt = randint(0,3) - lastDirectionInt % 3
        direction = directions[directionInt]
        xDir = direction[0]
        zDir = direction[1]
        i += 1

    # track the last direction
    lastDirectionInt = directionInt

    # iterate over the pathLength and ceate a 2 wide path
    for i in xrange(0, pathLength):
        try:
            if levelGrid[xStart][zStart][0] != 1:
                levelGrid[xStart][zStart] = [2, 64]
                if zDir == 0:
                    levelGrid[xStart][zStart + 1] = [2, 64]
                elif xDir == 0:
                    levelGrid[xStart + 1][zStart] = [2, 64]
        except Exception as e:
            print(str(e))

        # increment the location to build the next paths
        xStart += xDir
        zStart += zDir

    return xStart, zStart

# Level out the terrain around the plot to look more adapted
def levelTerrain(level, levelGrid):
    global minx, minz
    for location in buildingLocations:
        xDest = location[0]
        zDest = location[1]
        width = location[2] / 2
        height = location[3]

        # remove / add ground as necessary to make the plots look natural
        for x in range(xDest - width, xDest + width):
            for z in range(zDest - width, zDest + width):
                height = levelGrid[x][z][1]
                med = location[3]

                block = level.blockAt(x + minx, height, z + minz)
                data = 0
                if (block == 8 or block == 9):
                    modified_block_data = modifyWoodToSuitBiome([5,0], level.biomeAt(minx + x, minz + z))
                    block = modified_block_data[0]
                    data = modified_block_data[1]

                while(height < med):
                    utilityFunctions.setBlock(level, (block, data), x + minx, height, z + minz)
                    height += 1

                while(level.blockAt(x + minx, height, z + minz) != 0) and (height > med):
                    utilityFunctions.setBlock(level, (0, 0), x + minx, height, z + minz)
                    height -= 1
                    
        # apply the median heights
        for x in range(xDest - width, xDest + width):
            for z in range(zDest - width, zDest + width):
                levelGrid[x][z][1] = med

        i = 0
        q = 18
        while (i < 3):
            i += 1
            j = i - 1
            q += 1
            for x in xrange(xDest - width - i, xDest + width + i):
                for z in xrange(zDest - width - i, zDest + width + i):
                    if ((x < xDest - width - j) or (x > xDest + width + j - 1)) or ((z < zDest - width - j) or (z > zDest + width + j - 1)):
                        if (x > 0 and x < len(levelGrid)) and (z > 0 and z < len(levelGrid[0])):
                            height = getHeight(level, minx + x, minz + z, False)
                            modify = determineNeighbourHeights(level, minx + x, minz + z, height)
                            block = level.blockAt(x + minx, height, z + minz)

                            newHeight = getHeight(level, minx + x, minz + z) + modify
                            levelGrid[x][z][1] = newHeight
                            while(height < newHeight):
                                utilityFunctions.setBlock(level, (block, 0), x + minx, height, z + minz)
                                height += 1

                            while(level.blockAt(x + minx, height, z + minz) != 0) and (height > newHeight):
                                utilityFunctions.setBlock(level, (0, 0), x + minx, height, z + minz)
                                height -= 1

def determineNeighbourHeights(level, midX, midZ, height):
    for x in xrange(midX - 1, midX + 1):
        for z in xrange(midZ - 1, midZ + 1):
            block = level.blockAt(x, height, z)
            if block == 0:
                block = level.blockAt(x , height - 1, z)
                if block == 0:
                    return -1  
            else:
                block = level.blockAt(x, height + 1, z)
                if block != 0:
                    return 1

    return 0

# this function modifies wood, wood planks and stairs to the appropriate wood type based on the biome
def modifyWoodToSuitBiome(block_data, biome_id):
    block_id = block_data[0]
    block_second_id = block_data[1]

    if block_id == "17" or block_id == "5" or block_id == "53":
        if block_id == "53":
            if biome_id in stairBlockTypePerBiome:
                return [stairBlockTypePerBiome[biome_id], block_second_id]
            else:
                return block_data
        else:
            if biome_id in woodTypePerBiome:
                return [block_id, woodTypePerBiome[biome_id]]
            else:
                return block_data
    else:
        return block_data


# Build the bulids per house plot
def bulidBuildings(level, xLoc, zLoc):
    building_factory = BuildingFactory()

    for location in buildingLocations:
        xDest = location[0]
        zDest = location[1]
        width = location[2] / 2
        height = location[3] + 1

        blueprint = building_factory.choose_building(location[2])
        if blueprint:
            building = blueprint["building"]
            height += blueprint["height"]
            biome_id = 0
            for building_level in building:
                x_idx = 0
                for x in xrange(xDest - width, xDest + width):
                    z_idx = 0
                    for z in xrange(zDest - width, zDest + width):
                        block_data = building_level[x_idx][z_idx].split(":")
                        block = block_data[0]

                        if x_idx == 0 and z_idx == 0:
                            biome_id = level.biomeAt(xLoc + x, zLoc + z)

                        if block != "0":
                            modified_block_data = modifyWoodToSuitBiome(block_data, biome_id)
                            block = modified_block_data[0]
                            data = modified_block_data[1]

                            utilityFunctions.setBlock(level, (int(block), int(data)), xLoc + x, height, zLoc + z)

                        z_idx += 1
                    x_idx += 1
                height += 1
