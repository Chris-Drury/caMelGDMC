from random import randint, choice

from buildingArrays import BuildingFactory
import utilityFunctions
from editortools.clone import CloneTool as ct
from pymclevel import alphaMaterials

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

    # Place the grid on the terrain
    print("Generating terrain...")
    overlayGrid(levelGrid, level)

    # build houses
    print("Generating buildings...")
    bulidBuildings(level, minx, minz)

# Apply the levelGrid to the terrain
def overlayGrid(levelGrid, level):
    global minx, minz
    xLoc = minx

    for x in levelGrid:
        zLoc = minz
        for y in x:
            layoutType = y[0]
            height = y[1]
            if layoutType == 1: 
                # house plots
                block = 5 if (level.blockAt(xLoc, height, zLoc) == 9) else 2

                utilityFunctions.setBlock(level, (block, 0), xLoc, height, zLoc)
            elif layoutType == 2:
                # paths
                height = getHeight(level, xLoc, zLoc, False)
                block = 5 if (level.blockAt(xLoc, height, zLoc) == 9) else 208

                utilityFunctions.setBlock(level, (block, 0), xLoc, height, zLoc)
            zLoc += 1
        xLoc += 1

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
        
        # remove / add ground as necessary to make the plots look natural
        for x in range(xDest - width, xDest + width):
            for z in range(zDest - width, zDest + width):
                height = levelGrid[x][z][1]
                if (height < med):

                    block = level.blockAt(x + minx, height, z + minz)
                    block = 3 if (block == 2) else block

                    while(height < med):
                        utilityFunctions.setBlock(level, (block, 0), x + minx, height, z + minz)
                        height += 1

                if (height > med):
                    while(level.blockAt(x + minx, height, z + minz) != 0) and (height > med):
                        utilityFunctions.setBlock(level, (0, 0), x + minx, height, z + minz)
                        height -= 1


        # apply the median heights
        for x in range(xDest - width, xDest + width):
            for z in range(zDest - width, zDest + width):
                levelGrid[x][z][1] = med                

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

# Build the bulids per house plot
def bulidBuildings(level, xLoc, zLoc):
    building_factory = BuildingFactory()

    for location in buildingLocations:
        xDest = location[0]
        zDest = location[1]
        width = location[2] / 2
        height= location[3] + 1

        blueprint = building_factory.choose_building(location[2])
        if blueprint:
            building = blueprint["building"]
            height += blueprint["height"]
            for building_level in building:
                x_idx = 0
                for x in xrange(xDest - width, xDest + width):
                    z_idx = 0
                    for z in xrange(zDest - width, zDest + width):
                        block_data = building_level[x_idx][z_idx].split(":")
                        block = block_data[0]
                        data = block_data[1]

                        if block != "0":
                            utilityFunctions.setBlock(level, (int(block), int(data)), xLoc + x, height, zLoc + z)
                        
                        z_idx += 1
                    x_idx += 1
                height += 1
