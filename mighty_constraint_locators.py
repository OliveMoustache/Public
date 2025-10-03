##### mighty_constraint_locator.py
##### v1.2

##### Procedure to constraint a locator to all the selected controls

#### This will be the first step to copy a control position to world before baking the controls back
####     after modifying the root placement of a control.

#### You might want to customize section 1 to group your constraints where required by your pipeline
### 
#### TODO
###        1. Naming of the constraints doesn't work properly => issue for mighty_locators_to_CTRLs.py
###         seems to be a problem with the namespace, works fine without Namespace
###         or maybe not, output created : mighty_Loc_fc_boss_anim_1:ARM_R_wristIk_CTL 
###         mighty_Loc_ is added to the name which works ok I think
###        2. Save the locators and controls name in a text file or global variable to be reused if/when baking back
###         the controls to the locator 
### v1.2 added output for each constraint created.

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
    print ( 'Locator creation for the following control : ' + sel[i] )
    print ( 'Locator created : ' + mightyLocator )    
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
