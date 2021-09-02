## Locator match position
## Create a locator with a name based on the object and snap it to the position of that object
import maya.cmds as cmds
posGrab = cmds.ls(selection=True)
locName =  posGrab[0] + '_Loc' 
cmds.spaceLocator ( n =  locName  )
cmds.parent( locName,posGrab, r = 1 )
cmds.parent( locName, w =1 )
