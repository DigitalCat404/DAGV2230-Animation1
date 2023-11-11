import maya.cmds as cmds


def ChangeOverrideColor(color):
    selection = cmds.ls(selection=True)

    # Change the override color for each object
    for obj in selection:
        shapes = cmds.listRelatives(obj, shapes=True) or []
        for shape in shapes:
            cmds.setAttr(shape + ".overrideEnabled", 1)
            cmds.setAttr(shape + ".overrideColor", color)


ChangeOverrideColor(4)