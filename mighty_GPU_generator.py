import maya.cmds as cmds
import maya.mel as mel
from maya.mel import eval

def mighty_GPU_generator(): 
    ## Setting up the variables
##    dir_path = ?
    current_file_name = cmds.file(sceneName=True, query=True, shortName=1 )
    minTime = cmds.playbackOptions( q = 1, minTime = 1 )
    maxTime = cmds.playbackOptions( q = 1, maxTime = 1 ) 
    mighty_GPU_generator_selection = cmds.ls( sl =True )
    print ("Object selected is : " +  mighty_GPU_generator_selection[0])
    GPUcacheName = current_file_name + mighty_GPU_generator_selection[0]
    cmds.gpuCache ( Rosie:Geometries, startTime = minTime, endTime = maxTime, optimize = 1, optimizationThreshold = 40000, writeMaterials = 1, dataFormat = ogawa, directory = "/alembic", fileName = 'GPUcacheName', directory=‘dir_path’)
##    cmds.gpuCache ( Rosie:Geometries, startTime = minTime, endTime = maxTime, optimize = 1, optimizationThreshold 40000, writeMaterials, dataFormat ogawa, directory = "/alembic", fileName = 'GPUcacheName', directory=‘dir_path’)


mighty_GPU_generator()


asset_full_name = referenceQuery ( namespace = true `ls -sl`

asset_full_name =  cmds.ls( sl =True )
print asset_full_name
fileName = asset_full_name.split(':')[0]
 
 
 
#### Mel below  




current_file_name = cmds.file(sceneName=True, query=True, shortName=1 )
minTime = cmds.playbackOptions( q = 1, minTime = 1 )
maxTime = cmds.playbackOptions( q = 1, maxTime = 1 ) 
mighty_GPU_generator_selection = cmds.ls( sl =True )
GPUcacheName = current_file_name + mighty_GPU_generator_selection[0]
stringGPU = ('gpuCache -startTime ' + str(minTime) + ' -endTime ' + str(maxTime) + ' -optimize -optimizationThreshold 40000 -writeMaterials -dataFormat ogawa -directory "/alembic" -fileName "' + GPUcacheName + '.abc" Rosie:Geometries;')
print stringGPU
mel.eval(stringGPU)

cmds.file ( import = 'C:/Users/artiste/Documents/maya/projects/default/cache/alembic/BDG_205_22_Rosie.abc' )
cmds.file ( unloadReference = 'RosieRN' )
