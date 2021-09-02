## Locator match position
## Create a locator with a name based on the object and snap it to the position of that object
import maya.cmds as cmds
posGrab = cmds.ls(selection=True)
locName =  posGrab[0] + '_Loc' 
cmds.spaceLocator ( n =  locName  )
cmds.parent( locName,posGrab, r = 1 )
cmds.parent( locName, w =1 )


## Second method with Xform
'''
## Locator match position with Xform command
## Create a locator with a name based on the object and snap it to the position of that object
import maya.cmds as cmds
posGrab = cmds.ls(selection=True)
locName =  posGrab[0] + '_Loc' 
cmds.spaceLocator ( n =  locName  )

clusterPos = cmds.xform( posGrab, query=True, translation=True, worldSpace=True )
clusterRot = cmds.xform( posGrab, query=True, rotation=True, worldSpace=True )
cmds.xform ( locName, t= (clusterPos[0],clusterPos[1], clusterPos[2]) )
cmds.xform ( locName, ro= (clusterRot[0],clusterRot[1], clusterRot[2]) )

'''
