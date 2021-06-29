import maya.cmds as cmds
import maya.mel as mel
from maya.mel import eval

def mighty_GPU_generator(): 
    ## Setting up the variables
    ##    dir_path = ?
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

GPUcacheName = ( mighty_GPU_cache_prefix + "_cache_" + nameSpaceString)

## test gpuCache command line
cmds.gpuCache ( nameSpaceString + ":Geometries", startTime = minTime, endTime = maxTime, optimize = 1, optimizationThreshold = 40000, directory = "", fileName = GPUcacheName )
cachePath = ( "C:/Users/artiste/Documents/maya/projects/default/cache/alembic/" + GPUcacheName + ".abc" )

# ==============
# - Load Cache -
# ==============

# Create Cache Node
##cacheNode = cmds.createNode('gpuCache',name=cacheName+'Cache')
cacheNode = cmds.createNode('gpuCache',name='Cache')
cacheParent = cmds.listRelatives(cacheNode,p=True,pa=True)
cacheParent = cmds.rename(cacheParent,cacheName)

# Set Cache Path
cmds.setAttr(cacheNode+'.cacheFileName',cachePath,type='string')

# ==============
# - End Load Cache -
# ==============


cmds.file ( cachePath )

## working example cmds.file ( 'N:/02_SAISON_2/03_FABRICATION/ASSETS/Character/' + charName + '/rigging/pub/BDG__Character__' + charName + '__rigging.ma', reference = True, type = "mayaAscii", namespace = charName  )

cmds.file ( unloadReference = nameSpaceString + "RN" )

mighty_GPU_generator()




