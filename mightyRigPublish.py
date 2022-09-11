## mighty_rig_publish.py

## v 1 This version.

###### How to Use ##################
## This script is to back up and export the current mGear file
## and save/rename it into a Publish children folder
## The script will simply delete the guide group
##
## Copy the mightyRigPublish.py file into your script folder 
## 
## Call the script by the procedure name
## mightyRigPublish()

## TODO
## Look for Publish folder and create one if doesn't exist

import os
import pymel.core as pm
import maya.cmds as cmds

def mightyRigPublish():

    ## Get workfile name
    basename = os.path.basename(pm.sceneName())
    ## Get filename without extenstion
    filename = os.path.splitext(basename)[0]
    ## Get directory
    directory = os.path.dirname(pm.sceneName())
    print ( directory )

    ## Save workfile
    cmds.file ( save=True, type='mayaAscii' )
    print ( '\n //////////////////////////        Current file backed up as: ' + basename + '/////////////////////' )

    ## Rename publish file
    cmds.file ( rename = 'Scenes/Publish/' + filename + '_PUBLISH' ) 
    
    #### Deleting the mGear guids     
    cmds.delete ( 'guide' )

    ## Save publish file
    cmds.file ( save=True, type='mayaAscii' )
    print ( '\n////////////////////    1. scene renamed to *_PUBLISH     /////////////////\n' )
    print ( '////////////////////            Rig published         /////////////////\n' )

    ## Reopen work file
    print ( '////////////////////         Reopening workfile       /////////////////\n' )

    cmds.file ( basename, o = True )


mightyRigPublish()
