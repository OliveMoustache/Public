## Those are 3 functions to backup reRig's guides as a group of locators
## The guides in a new scene can then be snapped to those locators
## using either the Xform or constraint method. (I need to evaluate if both work)


import maya.cmds as cmds
import maya.mel as mel

## List of Master, left and center guides that have translation and rotation values
reRig_guides_list = [
'gdeReedMaster',
'gdeCogMaster',
'gdeSpineMaster',
'gdeSpineUp',
'gdeSpine00',
'gdeSpine01',
'gdeSpine02',
'gdeSpine03',
'gdeSpine04',
'gdeSpine05',

'gdeArmMasterLf',
'gdeArm00Lf',
'gdeArm01Lf',
'gdeArm02Lf',

'gdeHandMasterLf',
'gdeHand01Lf',
'gdeHand02Lf',

'gdeFingerAMasterLf',
'gdeFingerAUpLf',
'gdeFingerA00Lf',
'gdeFingerA01Lf',
'gdeFingerA02Lf',
'gdeFingerA03Lf',
'gdeFingerA04Lf',

'gdeFingerBMasterLf',
'gdeFingerBUpLf',
'gdeFingerB00Lf',
'gdeFingerB01Lf',
'gdeFingerB02Lf',
'gdeFingerB03Lf',
'gdeFingerB04Lf',

'gdeFingerCMasterLf',
'gdeFingerCUpLf',
'gdeFingerC00Lf',
'gdeFingerC01Lf',
'gdeFingerC02Lf',
'gdeFingerC03Lf',
'gdeFingerC04Lf',

'gdeFingerDMasterLf',
'gdeFingerDUpLf',
'gdeFingerD00Lf',
'gdeFingerD01Lf',
'gdeFingerD02Lf',
'gdeFingerD03Lf',
'gdeFingerD04Lf',

'gdeFingerEMasterLf',
'gdeFingerEUpLf',
'gdeFingerE00Lf',
'gdeFingerE01Lf',
'gdeFingerE02Lf',
'gdeFingerE03Lf',

'gdeArmClavicleLf',
'gdeClavicleRotMasterLf',
'gdeClavicleTransMasterLf',

'gdeNeckMaster',
'gdeNeckUp',
'gdeNeck00',
'gdeNeck01',
'gdeNeck02',

'gdeHeadMaster',
'gdeHead00',
'gdeHead01',
'gdeHeadUp',

'gdeFaceMaster',
'gdeJaw00',
'gdeJaw01',
'gdeUpperJaw00',
'gdeFace00Upper',
'gdeFace00Lower',
'gdeChin',
'gdeMentalis',
'gdeJaw00Squash',
'gdeJaw00LowerSquash',
'gdeFace00Squash',
'gdeFace00UpperSquash',
'gdeFaceGlobalSquash',
'gdeFaceLowerSquash',
'gdeFaceUpperSquash',

'gdeNoseMaster',
'gdeNoseUp',
'gdeNoseTipCt',
'gdeNose00BridgeCt',
'gdeNose01BridgeCt',
'gdeNoseNostrilCt',
'gdeNoseBaseCt',
'gdeNoseNostrilLf',

'gdeEarMasterLf',
'gdeEarUpLf',
'gdeEar00Lf',
'gdeEar01Lf',
'gdeEar02Lf',

'gdeUpperCheekMasterLf',
'gdeUpperCheekUpLf',
'gdeUpperCheek00Lf',
'gdeUpperCheek01Lf',
'gdeUpperCheek02Lf',

'gdeCheekMasterLf',
'gdeCheekLf',
'gdeCheekFleshyLf',

'gdeEyebrowMasterLf',
'gdeEyebrow01Lf',
'gdeEyebrow02Lf',
'gdeEyebrow03Lf',
'gdeEyebrow04Lf',

'gdeEyeMasterLf',
'gdeEyeUpLf',
'gdeEyeAimLf',
'gdeEyeIrisLf',
'gdeEye00SocketLf',
'gdeEye01SocketLf',
'gdeEye02SocketLf',
'gdeEye03SocketLf',
'gdeEye04SocketLf',
'gdeEye05SocketLf',
'gdeEye06SocketLf',
'gdeEye07SocketLf',
'gdeEye08SocketLf',
'gdeEye09SocketLf',
'gdeEye10SocketLf',
'gdeEye11SocketLf',

'gdeUpperTeethMaster',
'gdeUpperTeeth00GumsLf',
'gdeUpperTeeth01GumsLf',
'gdeUpperTeeth00TeethLf',
'gdeUpperTeeth01TeethLf',
'gdeUpperTeeth00MidLf',
'gdeUpperTeeth01MidLf',
'gdeUpperTeeth00GumsCt',
'gdeUpperTeeth00TeethCt',
'gdeUpperTeeth00MidCt',

'gdeLowerTeethMaster',
'gdeLowerTeeth00GumsLf',
'gdeLowerTeeth01GumsLf',
'gdeLowerTeeth00TeethLf',
'gdeLowerTeeth01TeethLf',
'gdeLowerTeeth00MidLf',
'gdeLowerTeeth01MidLf',
'gdeLowerTeeth00GumsCt',
'gdeLowerTeeth00TeethCt',
'gdeLowerTeeth00MidCt',

'gdeTongueMaster',
'gdeTongueUp',
'gdeTongue00Ct',
'gdeTongue00Lf',
'gdeTongue01Ct',
'gdeTongue01Lf',
'gdeTongue02Ct',
'gdeTongue02Lf',
'gdeTongue03Ct',
'gdeTongue03Lf',
'gdeTongue04Ct',
'gdeTongue04Lf',
'gdeTongue05Ct',
'gdeTongue05Lf',

## beware the following only have translation locked
'gdeLipsMaster',
'gdeLipsUpperCt',
'gdeLipsLowerCt',
'gdeLips01UpperLf',
'gdeLips01LowerLf',
'gdeLips00UpperLf',
'gdeLips00LowerLf',
'gdeLipsCornerLf']

    
    
def snapLocators2Guides(object): 
    ## Snap Locators ###########################
    ## This is the script to create then snap some Locators to the Guides
  
    ## create the Guides Locators group to export if it doesn't already exists
    if cmds.objExists('Guides_Loc_export'):
        print 'Guides loc group exists'
    else:
        cmds.group( em=True, name='Guides_Loc_export')
    
    for i in reRig_guides_list:
        locName =  i + '_Loc' 
        cmds.spaceLocator ( n =  locName  )
        cmds.parent( locName,'Guides_Loc_export' ) 
          
        clusterPos = cmds.xform( i, query=True, translation=True, worldSpace=True )
        clusterRot = cmds.xform( i, query=True, rotation=True, worldSpace=True )
        cmds.xform ( locName, t= clusterPos, worldSpace=True )
        cmds.xform ( locName, ro= clusterRot, worldSpace=True )
        ## increment the list
    
    cmds.select ( 'Guides_Loc_export' )
    print '///////////// Guides_Loc_export group ready for export //////////////\n'
    


    
    
def snapGuides2LocsXform(object): 
    ## Snap Guides ###########################
    ## This is the script to snap the Guides to the Locators

    ## We are looping the snapping of the guides to the locators
    for i in reRig_guides_list:
        locName =  i + '_Loc' 
        print locName      
        print i
        clusterPos = cmds.xform( locName, query=True, translation=True, worldSpace=True )
        clusterRot = cmds.xform( locName, query=True, rotation=True, worldSpace=True )
        cmds.xform ( i,  t= clusterPos, worldSpace=True  )
        cmds.xform ( i, ro= clusterRot, worldSpace=True  )
    
    cmds.select ( 'Guides_Loc_export' )
    print '///////////// The guides have been snapped to the Locators (xform method) //////////////\n'





def snapGuides2LocsConst(object): 
    ## Snap Guides ###########################
    ## This is the script to snap the Guides to the Locators using Constraints !!!!
    #### test with constraints instead
         
    for i in reRig_guides_list:
        locName =  i + '_Loc' 
        print locName      
        print i
        constrName = 'mighty_const_' + i
        cmds.parentConstraint( locName, i, n = constrName  )
        cmds.delete ( constrName )
    
    print '///////////// The guides have been snapped to the Locators (Constraint method) //////////////\n'




snapLocators2Guides(object)
snapGuides2LocsXform(object)
snapGuides2LocsConst(object)    
    
    
