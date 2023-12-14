import maya.cmds as cmds
import random
import pymel.core as pm


class RandomPlacement:

    def __init__(self):
        self.dupeCount = 1
        self.minX = 0
        self.maxX = 0
        self.minY = 0
        self.maxY = 0
        self.minZ = 0
        self.maxZ = 0

    def create(self):
        print("Opening menu")

        win = pm.window(title="Random Placement Generator")
        pm.rowColumnLayout(numberOfColumns=7, width=100)

        pm.text(label='Dupe Count')
        pm.text(label='Min X')
        pm.text(label='Max X')
        pm.text(label='Min Y')
        pm.text(label='Max Y')
        pm.text(label='Min Z')
        pm.text(label='Max Z')

        dupeCountText = cmds.intField(minValue=1)
        cmds.intField(dupeCountText, edit=True, changeCommand=lambda *args: self.storedupeCount(dupeCountText))

        minXText = pm.intField()
        pm.intField(minXText,edit=True,changeCommand=lambda *args: self.storeminX(minXText))

        maxXText = pm.intField()
        pm.intField(maxXText,edit=True,changeCommand=lambda *args: self.storemaxX(maxXText))

        minYText = pm.intField()
        pm.intField(minYText,edit=True,changeCommand=lambda *args: self.storeminY(minYText))

        maxYText = pm.intField()
        pm.intField(maxYText,edit=True,changeCommand=lambda *args: self.storemaxY(maxYText))

        minZText = pm.intField()
        pm.intField(minZText,edit=True,changeCommand=lambda *args: self.storeminZ(minZText))

        maxZText = pm.intField()
        pm.intField(maxZText,edit=True,changeCommand=lambda *args: self.storemaxZ(maxZText))

        goButton = pm.button(label="Generate", command=lambda *args: self.generate())

        pm.text(label=' Upper bound is not inclusive')

        pm.showWindow(win)

    def getdupeCount(self):
        return self.dupeCount

    def getminX(self):
        return self.minX

    def getmaxX(self):
        return self.maxX

    def getminY(self):
        return self.minY

    def getmaxY(self):
        return self.maxY

    def getminZ(self):
        return self.minZ

    def getmaxZ(self):
        return self.maxZ

    def storedupeCount(self,dupeCountText):
        self.dupeCount = cmds.intField(dupeCountText, q=True, value=True)

    def storeminX(self, minXText):
        self.minX = cmds.intField(minXText, q=True, value=True)

    def storemaxX(self, maxXText):
        self.maxX = cmds.intField(maxXText, q=True, value=True)

    def storeminY(self, minYText):
        self.minY = cmds.intField(minYText, q=True, value=True)

    def storemaxY(self, maxYText):
        self.maxY = cmds.intField(maxYText, q=True, value=True)

    def storeminZ(self, minZText):
        self.minZ = cmds.intField(minZText, q=True, value=True)

    def storemaxZ(self, maxZText):
        self.maxZ = cmds.intField(maxZText, q=True, value=True)

    def generate(self):
        selection = cmds.ls(selection=True)

        if (self.dupeCount < 1):
            print("Nothing selected")

        elif selection == []:
            print("Nothing selected")

        else:
            for obj in selection:
                for dupe in range(self.dupeCount):
                    duplicate = cmds.duplicate(obj, name=obj + "_Dupe1")
                    rand_x = random.randrange(self.minX, self.maxX)
                    rand_y = random.randrange(self.minY, self.maxY)
                    rand_z = random.randrange(self.minZ, self.maxZ)
                    cmds.xform(duplicate, ws=True, t=[rand_x, rand_y, rand_z])
                    print("Created " + str(dupe))

            print("Done!")

#randomStuff = RandomPlacement()
#randomStuff.create()