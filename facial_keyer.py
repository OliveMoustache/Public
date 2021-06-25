import maya.cmds as cmds
import maya.mel as mel
from maya.mel import eval

def phonemesKeyer(object): 
    startTime = cmds.date (t = True )
    ### List of characters for which to generate mouth shapes    
    Char_list = [
    'Basil',
    'Berry',
    'Berry_Tooth',
    'Biva',
    'Candice',
    'Casimir',
    'Catchup',
    'Catchup_Necklace',
    'Edmund',
    'Edmund_Bag',
    'Grandma',
    'Grandpa',
    'Loudo',
    'Lucien',
    'Margaret',
    'Martis',
    'Mary',
    'Pico',
    'Pierrette',
    'Rosie',
    'Rosie_Yellow',
    'Scout_Crown',
    'Scout_Medal',
    'Scout_Whistle',        
    'Scoutbadger',
    'Sourpuss',    
    'Woods_Crown',
    'Woodsy_Necklace',    
    'Woods_Medal',
    'Woodsy',
    'Woodsy_Splint'
     ]

    
    for charName in Char_list:
        ### Load References        
        # Import Phonemes scenes assets
        cmds.file ( "scenes    for charName in Char_list:/MouthShapes/Phonemes_Scene.ma", reference = True, type = "mayaAscii", namespace = 'Phonemes_Scene'  )
        # Import Characters
        cmds.file ( 'N:/02_SAISON_2/03_FABRICATION/ASSETS/Character/' + charName + '/rigging/pub/BDG__Character__' + charName + '__rigging.ma', reference = True, type = "mayaAscii", namespace = charName  )
        print '\n/////////////////////////////////////////////'
        print '/////////////////////////////////////////////'
        print '////'
        print '//// 1. Character ' + charName + ' loaded ////'

        ## Regenerate UV tiles
        eval( 'generateAllUvTilePreviews;' )

        ## Creating zero keys on bookmarks
        Phonem_keys = [ '1', '10', '20', '30', '40', '50', '60', '70', '80' ]
        for i in Phonem_keys:
            cmds.setKeyframe( charName + ':face_A_fac_ctl', attribute = 'translateY', v = 0, t = i , itt = 'linear' )
            cmds.setKeyframe( charName + ':face_O_fac_ctl', attribute = 'translateY', v = 0, t = i , itt = 'linear' )
            cmds.setKeyframe( charName + ':face_CDGK_fac_ctl', attribute = 'translateY', v = 0, t = i , itt = 'linear' )
            cmds.setKeyframe( charName + ':face_Fv_fac_ctl', attribute = 'translateY', v = 0, t = i , itt = 'linear' )
            cmds.setKeyframe( charName + ':face_MBP_fac_ctl', attribute = 'translateY', v = 0, t = i , itt = 'linear' )
            cmds.setKeyframe(  charName + ':face_L_fac_ctl', attribute = 'translateY', v = 0, t = i , itt = 'linear' )
            cmds.setKeyframe( charName + ':face_U_fac_ctl', attribute = 'translateY', v = 0, t = i , itt = 'linear' )    
        
            ## Keying the phonemes
            cmds.setKeyframe( charName + ':face_A_fac_ctl', attribute = 'translateY', v = 1, t = 10 , itt = 'linear' )
            cmds.setKeyframe( charName + ':face_O_fac_ctl', attribute = 'translateY', v = 1, t = 20 , itt = 'linear' )
            cmds.setKeyframe( charName + ':face_CDGK_fac_ctl', attribute = 'translateY', v = 1, t = 30 , itt = 'linear' )
            cmds.setKeyframe( charName + ':face_Fv_fac_ctl', attribute = 'translateY', v = 1, t = 40 , itt = 'linear' )
            cmds.setKeyframe( charName + ':face_MBP_fac_ctl', attribute = 'translateY', v = 1, t = 50 , itt = 'linear' )
            cmds.setKeyframe( charName + ':face_L_fac_ctl', attribute = 'translateY', v = 1, t = 60 , itt = 'linear' )
            cmds.setKeyframe( charName + ':face_U_fac_ctl', attribute = 'translateY', v = 1, t = 70 , itt = 'linear' )   
        print '//// 2. Phonemes keyed ////'    
                
        ### Get Head pos then Xform Cam to it ( not quite ready, will need to use the BBox to offset the CAM placement
        FKHead_pos = cmds.xform ( charName + ':FKHead_M_CTRL', query = True, translation = True, worldSpace = True )
        FKHead_posXYZ = FKHead_pos[0], FKHead_pos[1], 0   
        #cmds.xform ( "Cam_offseter", t = FKHead_posXYZ )
        
        ## Playblast
        playblastPath = "scenes/MouthShapes/" + charName + "_phonemes"
#        cmds.playblast ( filename = playblastPath, forceOverwrite = 1, format = "qt", viewer = 0,  startTime = 0, endTime = 90,  clearCache = 1,
#        showOrnaments = 0, offScreen = 1, framePadding = 4, percent = 100, compression = "H.264", quality = 100 )
        print '//// 3. Playblast phoneme file generated for ' + charName + ' ////'

        ### Saving Phoneme Maya file
        # Unload Phonemes scenes assets
        cmds.file ( "scenes/MouthShapes/Phonemes_Scene.ma", removeReference = True   )
        # Actual saving of file        
        cmds.file( rename='scenes/MouthShapes/' + charName + '_Phonemes.ma' )
        cmds.file( save=True, type='mayaAscii' )
        print '//// 4. Maya Phoneme file generated for ' + charName + ' ////'
        
        ### Unload Reference
        cmds.file ( 'N:/02_SAISON_2/03_FABRICATION/ASSETS/Character/' + charName + '/rigging/pub/BDG__Character__' + charName + '__rigging.ma', removeReference = True )
        print '//// 5. Reference ' + charName + ' unloaded ////\n'

    endTime = cmds.date( t = True )
    print ('//////         Phoneme Keyer process started at ' + startTime + '///// ')
    print ('//////         Phoneme Keyer process completed at ' + endTime + '///// ')
    print '////'
    print '////////////////////////////////////////////////////////////////////////////////////////////'
    print '////////////////////////////////////////////////////////////////////////////////////////////\n'

phonemesKeyer(object)

