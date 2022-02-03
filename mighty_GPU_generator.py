#
#  Mighty GPU generator v1.1
#  2021 06 29
#  mighty_GPU_generator.py
#  by Olivier Ladeuix
#  www.olivier-ladeuix.com/blog

#    Switches the rig to a GPU cache representation

# /////////// How to install  //////////////////////
#     Place the script in your scripts folder
#     Do a rehash or restart Maya for Maya to load the script

# /////////// How to use  //////////////////////
#
#     1. Select any control from the rig you want to GPU cache just so you can speed up the scene and focus
#         on other characters
#     2. Run the script with the following command:
#            import mighty_GPU_generator
#            mighty_GPU_generator.mighty_gpu_generator()
#        You could also use a hotkey
#     3. When done, reload the reference from the reference editor.
#
# ////////////////////////////////

# ////////////////////////////////

# CHANGELOG:
# 2021 07 27    v1.1     File path changed to reflect new Windows sessions.
# 2021 06 29    v1.0
#

# Room for improvement :
#
#

# /// FAQ
# ///
# ///
# ////////////////////////////////

import os

import maya.cmds as cmds


def mighty_gpu_generator():
    """ Definition of the variables
    Get the namespace
    """
    selection_buffer = cmds.ls(selection=True)
    if len(selection_buffer) != 1:
        return cmds.warning("########  You have to select an character ########")

    mighty_gpu_generator_selection = selection_buffer[0]
    name_space_string = mighty_gpu_generator_selection.split(':')[0]
    cache_name = name_space_string + "_GPU_cache"

    if cmds.objExists(cache_name):
        cmds.delete(cache_name)
        print("######## {} deleted ########".format(cache_name))

    # Get the filename as prefix
    current_file_name = cmds.file(sceneName=True, query=True, shortName=True)
    mighty_gpu_cache_prefix = current_file_name.split('_animation_')[0]

    # Get the timeline range
    min_time = cmds.playbackOptions(q=True, minTime=True)
    max_time = cmds.playbackOptions(q=True, maxTime=True)

    # Generate GPU cache file name with Prefix
    gpu_cache_file_name = "{0}_{1}_GPU_cache".format(mighty_gpu_cache_prefix, name_space_string)
    print("######## GPU Cache will be named {} ########".format(gpu_cache_file_name))

    # GPU cache processing
    cmds.gpuCache(name_space_string + ":Geometries", startTime=min_time, endTime=max_time,
                  optimize=True, optimizationThreshold=40000, directory="", fileName=gpu_cache_file_name)
    print("######## GPU Cache processed ########")

    # ==============
    # - Load Cache -
    # ==============
    # cachePath concatenation
    home_dir = os.environ['HOME']
    cache_path = "{0}/maya/projects/default/cache/alembic/{1}.abc".format(home_dir, gpu_cache_file_name)
    print("######## GPU Cache generated as " + cache_path + " ########")

    # Create Cache Node
    cache_node_name = name_space_string + "_GPU_cacheShape"
    cache_node = cmds.createNode('gpuCache', name=cache_node_name)
    cache_parent = cmds.listRelatives(cache_node, parent=True, path=True)
    cmds.rename(cache_parent, cache_name)

    # Load the GPU data into the cacheNode
    cmds.setAttr(cache_node+'.cacheFileName', cache_path, type='string')

    # ==============
    # - End Load Cache -
    # ==============
    # Unload the referenced rig
    cmds.file(unloadReference="CHAR_{}_1RN".format(name_space_string))
    print("######## Rig unloaded and GPU loaded ########")
