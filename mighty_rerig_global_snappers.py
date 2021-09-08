## mighty_rerig_global_snappers.py
## creator: Olivier Ladeuix
## 2021 09 04
## v1.1
## Olivier Ladeuix
## http://www.olivier-ladeuix.com/blog/

## Those are 3 functions to backup reRig's guides as a group of locators called "Guides_Loc_export"
## This group can be exported as a Maya file for backup and reimported in a new setup file

## You will then snap the guides from that news scene to those locators
## using either the Xform or constraint method. (I need to evaluate what is best, so far the
## xform method seems to be working perfectly

## When Importing the Guides_Loc_export group into the new scenes, make sure the namespace is off
## amd Clashing nodes set to resolve with an empty string just so we don't have any namespace added by Maya





import maya.cmds as cmds
import maya.mel as mel

## List of Master, left and center guides that have translation and rotation values
## The order is very important since the child guides get affected by the Master guides
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
'gdeFingerA00Lf',
'gdeFingerA01Lf',
'gdeFingerA02Lf',
'gdeFingerA03Lf',
'gdeFingerA04Lf',
'gdeFingerAUpLf',

'gdeFingerBMasterLf',
'gdeFingerB00Lf',
'gdeFingerB01Lf',
'gdeFingerB02Lf',
'gdeFingerB03Lf',
'gdeFingerB04Lf',
'gdeFingerBUpLf',

'gdeFingerCMasterLf',
'gdeFingerC00Lf',
'gdeFingerC01Lf',
'gdeFingerC02Lf',
'gdeFingerC03Lf',
'gdeFingerC04Lf',
'gdeFingerCUpLf',

'gdeFingerDMasterLf',
'gdeFingerD00Lf',
'gdeFingerD01Lf',
'gdeFingerD02Lf',
'gdeFingerD03Lf',
'gdeFingerD04Lf',
'gdeFingerDUpLf',

'gdeFingerEMasterLf',
'gdeFingerE00Lf',
'gdeFingerE01Lf',
'gdeFingerE02Lf',
'gdeFingerE03Lf',
'gdeFingerEUpLf',


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
'gdeEar00Lf',
'gdeEar01Lf',
'gdeEar02Lf',
'gdeEarUpLf',

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

'gdeLegMasterLf',
'gdeLeg00Lf',
'gdeLeg01Lf',
'gdeLeg02Lf',
'gdeLeg04Lf',
'gdeLeg05Lf',
'gdeLeg06Lf',
'gdeLegBankinLf',
'gdeLegBankoutLf',
'gdeLegBackLf',
'gdeLegBallLf',
'gdeLegTipLf',
'gdeLegHeelLf',
'gdeLegUpLf',

'gdeToeAMasterLf',
'gdeToeA00Lf',
'gdeToeA01Lf',
'gdeToeA02Lf',
'gdeToeAUpLf',

'gdeToeBMasterLf',
'gdeToeB00Lf',
'gdeToeB01Lf',
'gdeToeB02Lf',
'gdeToeBUpLf',

'gdeToeCMasterLf',
'gdeToeC00Lf',
'gdeToeC01Lf',
'gdeToeC02Lf',
'gdeToeCUpLf',

'gdeToeDMasterLf',
'gdeToeD00Lf',
'gdeToeD01Lf',
'gdeToeD02Lf',
'gdeToeDUpLf',

'gdeToeEMasterLf',
'gdeToeE00Lf',
'gdeToeE01Lf',
'gdeToeE02Lf',
'gdeToeEUpLf',

## beware the following have their translation locked
'gdeLipsMaster',
'gdeLipsUpperCt',
'gdeLipsLowerCt',
'gdeLips01UpperLf',
'gdeLips01LowerLf',
'gdeLips00UpperLf',
'gdeLips00LowerLf',
'gdeLipsCornerLf'
]

    
    
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

    locGrpLen = len( reRig_guides_list ) 
    
    cmds.select ( 'Guides_Loc_export' )
    print '///////////// Guides_Loc_export group ready for export //////////////'
    print '///////////// ' + str( locGrpLen) + ' locators mapped ////////////// \n'





def snapGuides2LocsXform(object): 
    ## Snap Guides ###########################
    ## This is the script to snap the Guides to the Locators using the xform method

    ## We are looping the snapping of the guides to the locators
    for i in reRig_guides_list:
        locName =  i + '_Loc' 
        clusterPos = cmds.xform( locName, query=True, translation=True, worldSpace=True )
        clusterRot = cmds.xform( locName, query=True, rotation=True, worldSpace=True )
        cmds.xform ( i,  t= clusterPos, worldSpace=True  )
        cmds.xform ( i, ro= clusterRot, worldSpace=True  )
    
    cmds.select ( 'Guides_Loc_export' )
    print '///////////// The guides have been snapped to the Locators (xform method) //////////////\n'





def snapGuides2LocsConst(object): 
    ## Snap Guides ###########################
    ## This is the script to snap the Guides to the Locators using Constraints, not sure if this is very smart
         
    for i in reRig_guides_list:
        locName =  i + '_Loc' 
        print locName      
        print i
        constrName = 'mighty_const_' + i
        cmds.parentConstraint( locName, i, n = constrName  )
        cmds.delete ( constrName )
    print '///////////// The guides have been snapped to the Locators (Constraint method) //////////////\n'




## Step 01. Start the function to snap a group of locators to your guides
snapLocators2Guides(object)

## Step 02.  Start the function to snap the new guides to the imported locators  (using the xform method)
snapGuides2LocsXform(object)

##  Step 02 alternate version. Start the function to snap the new guides to the imported locators  (using the constraint method.)
snapGuides2LocsConst(object)    





