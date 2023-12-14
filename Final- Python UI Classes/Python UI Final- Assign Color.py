import maya.cmds as cmds
import pymel.core as pm

class AssignColor:

    def __init__(self):
        self.color = 1

    def create(self):
        print("Opening menu")

        win = pm.window(title="Assign Override Color")
        pm.rowColumnLayout(numberOfColumns=1, width=400)

        pm.text(label='Color Index')

        colorText = cmds.intField(minValue=1,maxValue=31)
        cmds.intField(colorText, edit=True, changeCommand=lambda *args: self.storeColorText(colorText))

        goButton = pm.button(label="Change Color", command=lambda *args: self.ChangeOverrideColor())

        pm.showWindow(win)


    def getColorIndex(self):
        return self.color


    def storeColorText(self,colorText):
        self.color = cmds.intField(colorText, q=True, value=True)


    def ChangeOverrideColor(self):
        selection = cmds.ls(selection=True)

        if selection == []:
            print("Nothing selected")

        else:
            # Change the override color for each object
            for obj in selection:
                shapes = cmds.listRelatives(obj, shapes=True) or []
                for shape in shapes:
                    cmds.setAttr(shape + ".overrideEnabled", 1)
                    cmds.setAttr(shape + ".overrideColor", self.color)

            print("Done!")


#colorChanger = AssignColor()
#colorChanger.create()