import utilityFunctions
from editortools.clone import CloneTool as ct
from pymclevel import alphaMaterials

boundryBox = None # the bouding box to search in
filterOptions = None # the option dict

#inputs are taken from the user. Here I've just showing labels, as well as letting the user define
# what the main creation material for the structures is
inputs = (
	("CAMEL", "label"),
	("Material", alphaMaterials.Cobblestone), # the material we want to use to build the mass of the structures
	("Creator: CAMEL", "label"),
	)


def perform(level, box, options):
    filterOptions = options
    boundryBox = box

    for x in xrange(boundryBox.minx, boundryBox.maxx):
        for y in xrange(boundryBox.miny, boundryBox.maxy):
            for z in xrange(boundryBox.minz, boundryBox.maxz):
                # (level, (Block ID to change to, target's Block ID), x, y, z)
                utilityFunctions.setBlock(level, (1, 0), x, y, z)
