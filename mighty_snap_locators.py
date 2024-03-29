##### Procedure to create and snap a locator to all the selected guides
##### Later we could just grab them all from a hard coded list just so they are all done and in order

## make a list from the selection
guidesList = cmds.ls(selection=True)
## create the Guides Locators group to export if it doesn't already exists
if cmds.objExists('Guides_Loc_export'):
    print 'Guides loc group exists'
else:
    cmds.group( em=True, name='Guides_Loc_export')

listSize = len(guidesList)
increment = 0
for i in guidesList:
    locName =  guidesList[increment] + '_Loc' 
    cmds.spaceLocator ( n =  locName  )
    cmds.parent( locName,'Guides_Loc_export' )   
    clusterPos = cmds.xform( guidesList[increment], query=True, translation=True, worldSpace=True )
    clusterRot = cmds.xform( guidesList[increment], query=True, rotation=True, worldSpace=True )
    cmds.xform ( locName, t= (clusterPos[0],clusterPos[1], clusterPos[2]) )
    cmds.xform ( locName, ro= (clusterRot[0],clusterRot[1], clusterRot[2]) )
    ## increment the list
    increment = increment +1
cmds.select ( 'Guides_Loc_export' )
print '///////////// Guides_Loc_export group ready for export //////////////\n'
