##### Procedure to constraint a locator to all the selected controls
#### You might want to customize section 1 to group your constraints where required by your pipeline

#### TODO
#### Naming of the constraints doesn't work properly => issue for mighty_locators_to_CTRLs.py
### seems to be a problem with the namespace, works fine without Namespace


import maya.cmds as cmds 

print '\n ///////////// mightyConstraint_Locators script started ///////////// \n'
## make a list from the selection
ctrlList = cmds.ls(selection=True)

## create the Constraint Locators group if it doesn't already exists
if cmds.objExists('mightyConstraint_Locators'):
    print '///////////// mightyConstraint_Locators group already exists ///////////// \n'
else:
    cmds.group( em=True, name='mightyConstraint_Locators')

if ctrlList: 
	sel = ctrlList 
for i in range(len(sel)): 

    mightyLocator = 'mighty_Loc_' + sel[i]
    print ( 'Locator creation for ' + mightyLocator )
    #### creation of the locator
    cmds.spaceLocator ( name = mightyLocator ) 
    #### constraint of the locator to the control
    cmds.parentConstraint ( sel[i], mightyLocator, name = 'mighty_constraint_temp_parentConstraint__' + sel[i] )

    #### Section 1
    #### This is where you would customize the script and group the locators to your Sandbox or Temp group
    cmds.parent ( mightyLocator, 'mightyConstraint_Locators' )
    
    cmds.select ( mightyLocator )
    cmds.setKeyframe ( mightyLocator )
    cmds.setKeyframe( v=1, at='blend' )

print '\n ///////////// mightyConstraint_Locators and group created for select objects //////////////\n'
