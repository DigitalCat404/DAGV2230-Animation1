import maya.cmds as cmds
import random


# Shift + F1 to open up documentation about a command

def random_placement(dupeCount, minX, maxX, minY, maxY, minZ, maxZ):
    selection = cmds.ls(selection=True)

    if(selection == []):
        print("Nothing selected")

    else:
        for obj in selection:
            for dupe in range(dupeCount):
                duplicate = cmds.duplicate(obj,name=obj+"_Dupe1")
                rand_x = random.randrange(minX, maxX)
                rand_y = random.randrange(minY, maxY)
                rand_z = random.randrange(minZ, maxZ)
                cmds.xform(duplicate, ws=True, t=[rand_x, rand_y, rand_z])
                print("Created "+str(dupe))

        print("Done!")


random_placement(2, -2, 2, -2, 2, -2, 2)
