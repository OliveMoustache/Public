##### Procedure to create and snap a locator for each and to all the MANUALLY selected masters
### The locators will be placed in a group called 'Masters_locators'
## V 1.0
## 2022/09/01


## make a list from the selected Masters
mastersList = cmds.ls(selection=True)

## create the Masters_locators group 
if cmds.objExists('masters_loc_export'):
    print 'Masters_loc group exists'
else:
    cmds.group( em=True, name='masters_loc_export')

## initialize the loop
listSize = len(mastersList)
increment = 0

## Loop for the length of the array
for i in mastersList:
    locName =  mastersList[increment] + '_Loc' 
    cmds.spaceLocator ( n =  locName  )
    cmds.parent( locName,'masters_loc_export' )   
    clusterPos = cmds.xform( mastersList[increment], query=True, translation=True, worldSpace=True )
    clusterRot = cmds.xform( mastersList[increment], query=True, rotation=True, worldSpace=True )
    cmds.xform ( locName, t = clusterPos, worldSpace=True )
    cmds.xform ( locName, ro = clusterRot, worldSpace=True )
    ## increment the list for the loop
    increment = increment +1
    
cmds.select ( 'masters_loc_export' )
print '///////////// masters_loc_export group ready for export //////////////\n'
