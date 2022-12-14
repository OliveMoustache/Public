##### Procedure to constraint a locator to all the selected controls
#### You might want to customize section 1 to group your constraints where required by your pipeline

import maya.cmds as cmds 

## make a list from the selection
ctrlList = cmds.ls(selection=True)

## create the Constraint Locators group if it doesn't already exists
if cmds.objExists('Constraint_Loc'):
    print 'Constraint loc group exists'
else:
    cmds.group( em=True, name='mightyConstraint_Locators')

if ctrlList: 
	sel = ctrlList 
for i in range(len(sel)): 

    mightyLocator = 'mighty_Loc_' + sel[i]
    print ( 'Locator creation for ' + mightyLocator )
    
    cmds.spaceLocator ( name = mightyLocator ) 
    cmds.parentConstraint ( sel[i], mightyLocator, name = 'mighty_constraint_temp_parentConstraint_' + sel[i] )

    #### Section 1
    #### This is where you would customize the script and group the locators to your Sandbox or Temp group
    cmds.parent ( mightyLocator, 'mightyConstraint_Locators' )
    
cmds.select ( 'mightyConstraint_Locators' )

print '///////////// mightyConstraint_Locators and group created //////////////\n'
