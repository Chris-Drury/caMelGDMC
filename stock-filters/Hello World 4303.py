from random import randint, choice

from buildingArrays import BuildingFactory
import utilityFunctions
from editortools.clone import CloneTool as ct
from pymclevel import alphaMaterials

#inputs are taken from the user. Here I've just showing labels, as well as letting the user define
# what the main creation material for the structures is
inputs = (
	("CAMEL", "label"),
	("Material", alphaMaterials.Cobblestone), # the material we want to use to build the mass of the structures
	("Creator: CAMEL", "label"),
	)

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # right, up, left, down
lastDirectionInt = 5 # lets use this so it can never back track...
buildingLocations = [] # lets define a list of all locations that will need buildings

# The required method for MCEdit. This function will be what runs the filter.
def perform(level, box, options):
    filterOptions = options
    boundryBox = box

    # Build a 2D planning grid (does not consider height)
    levelGrid = [[0] * (boundryBox.maxz- boundryBox.minz) for i in range(boundryBox.minx, boundryBox.maxx)]

    # for step in xrange(0,4):
    generateLayout(levelGrid)
    
    xLoc = boundryBox.minz
    f= open("levelDemo.txt","w+")
    print("Generating terrain...")
    for x in levelGrid:
        zLoc = boundryBox.minx
        for y in x:
            if y == 0:
                f.write('X')
                utilityFunctions.setBlock(level, (2, 0), xLoc, 64, zLoc)
            elif y == 1: 
                f.write('.')
                utilityFunctions.setBlock(level, (45, 0), xLoc, 64, zLoc)
            elif y == 2:
                f.write('-')
                utilityFunctions.setBlock(level, (13, 0), xLoc, 64, zLoc)
            zLoc += 1
        xLoc += 1
        f.write("\n")
    f.close()

    # build houses
    print("Generating buildings...")
    bulidBuildings(level, boundryBox.minz, boundryBox.minx)

# This will create the layout on a 2D grid. The layout consists of house plots and roads/paths between each plot
def generateLayout(levelGrid):
    xSize = len(levelGrid)
    zSize = len(levelGrid[0])

    # create the first house. For now, always place it in the middle of the plot
    xEnd = xSize / 2
    zEnd = zSize / 2
    plotWidth = randint(4,8) / 2
    generateHousePlot(levelGrid, xEnd, zEnd, plotWidth)

    # begin branching a creating the rest of the village
    for houses in range(0,40):
        # Generate a path of a random length in a random direction
        xEnd, zEnd = generatePath(levelGrid, xEnd, zEnd, randint(8, 40),  randint(0, 3))

        # Create the width of the next house plot and check that it will fit int he boundingBox
        plotWidth = randint(4,8) / 2
            # TODO: Ideally, this would be replaced by a function call that would check
        if (xEnd + plotWidth > xSize) or (xEnd - plotWidth < 0):
            continue
        elif (zEnd + plotWidth > zSize) or (zEnd - plotWidth < 0):
            continue
        elif checkHousePlot(levelGrid, xEnd, zEnd, plotWidth):
            generateHousePlot(levelGrid, xEnd, zEnd, plotWidth)

# This will generate the house plot
def generateHousePlot(levelGrid, xDest, zDest, width):
    buildingLocations.append([xDest, zDest, width * 2, 64])
    for x in xrange(xDest - width, xDest + width):
        for z in xrange(zDest - width, zDest + width):
            levelGrid[x][z] = 1

# check that the house's plot will not override another plot
def checkHousePlot(levelGrid, xDest, zDest, width):
    for x in xrange(xDest - width, xDest + width):
        for z in xrange(zDest - width, zDest + width):
            if levelGrid[x][z] == 1:
                return False

    return True

# This will generate the paths, starting from the center of each house plot
def generatePath(levelGrid, xStart, zStart, pathLength, directionInt):
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
            xStart, zStart = generatePath(levelGrid, len(levelGrid) / 2, len(levelGrid[0]) / 2, pathLength, directionInt)
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
            if levelGrid[xStart][zStart] != 1:
                levelGrid[xStart][zStart] = 2
                if zDir == 0:
                    levelGrid[xStart][zStart + 1] = 2
                elif xDir == 0:
                    levelGrid[xStart + 1][zStart] = 2
        except Exception as e:
            print(str(e))
            
        # increment the location to build the next paths
        xStart += xDir
        zStart += zDir

    return xStart, zStart

def bulidBuildings(level, xLoc, zLoc):
    building_factory = BuildingFactory()

    for location in buildingLocations:
        xDest = location[0]
        zDest = location[1]
        width = location[2] / 2
        height= location[3] + 1

        building = building_factory.choose_building(location[2])

        if building:
            for building_level in building:
                x_idx = 0
                for x in xrange(xDest - width, xDest + width):
                    z_idx = 0
                    for z in xrange(zDest - width, zDest + width):
                        block_data = building_level[x_idx][z_idx].split(":")
                        block = block_data[0]
                        data = block_data[1]

                        utilityFunctions.setBlock(level, (int(block), int(data)), xLoc + x, height, zLoc + z)
                        
                        z_idx += 1
                    x_idx += 1
                height += 1
