##
##  Mighty GPU generator v1.0
##  2021 06 29
##  mighty_GPU_generator.py
##  by Olivier Ladeuix
##  www.olivier-ladeuix.com/blog

##    Switches the rig to a GPU cache representation

## /////////// How to install  //////////////////////
##     Place the script in your scripts folder
##     Do a rehash or restart Maya for Maya to load the script

## /////////// How to use  //////////////////////
##
##     1. Select any control from the rig you want to GPU cache just so you can speed up the scene and focus 
##         on other characters
##     2. Run the script with the following command: 
##            mighty_GPU_generator() 
##        You could also use a hotkey
##     3. When done, reload the reference from the reference editor.
##
##////////////////////////////////

## ////////////////////////////////

## CHANGELOG:
## 2021 06 29    v1.0 
##

## Room for improvement :
##
##

## /// FAQ
## /// 
## ///        
## ////////////////////////////////




import maya.cmds as cmds

def mighty_GPU_generator(): 
    ## Definition of the variables
    #### Get the namespace
    selection_buffer = cmds.ls( sl =True )
    mighty_GPU_generator_selection = str(selection_buffer[0])
    nameSpaceString =(mighty_GPU_generator_selection.split(':'))[0]
    print ("Object selected is : " +  nameSpaceString)
    
    #### Get the filename as prefix
    current_file_name = cmds.file(sceneName=True, query=True, shortName=1 )
    mighty_GPU_cache_prefix = (current_file_name.split('_animation_'))[0] 
    print mighty_GPU_cache_prefix
      
    #### Get the timeline range
    minTime = cmds.playbackOptions( q = 1, minTime = 1 )
    maxTime = cmds.playbackOptions( q = 1, maxTime = 1 ) 
    
    ## Generate GPU cache file name with Prefix
    GPUcacheFileName = ( mighty_GPU_cache_prefix + "_" + nameSpaceString + "_GPUcache")
    
    ## GPU cache processing
    cmds.gpuCache ( nameSpaceString + ":Geometries", startTime = minTime, endTime = maxTime, optimize = 1, optimizationThreshold = 40000, directory = "", fileName = GPUcacheFileName )
    
    ## path for work ### cachePath = ( "C:/Users/artiste/Documents/maya/projects/default/cache/alembic/" + GPUcacheName + ".abc" )
    ## path for home
    cachePath = ( "Z:/3d/Maui Rig/Maya/cache/alembic/" + GPUcacheFileName + ".abc" )
    
    # ==============
    # - Load Cache -
    # ==============
    # Create Cache Node
    cacheName = (nameSpaceString + "_GPU_cache")
    cacheNode = cmds.createNode('gpuCache',name='Cache')
    cacheParent = cmds.listRelatives(cacheNode,p=True,pa=True)
    cacheParent = cmds.rename(cacheParent, cacheName )
    # Load the GPU datas into the cacheNode
    cmds.setAttr(cacheNode+'.cacheFileName',cachePath,type='string')
    # ==============
    # - End Load Cache -
    # ==============
    
    ## Unload the referenced rig
    cmds.file ( unloadReference = nameSpaceString + "RN" )
    print "//////// Rig unloaded and GPU loaded /////////"


mighty_GPU_generator()
