import maya.cmds as cmds
import os



def get_default_path_snapshot(current_path=None):
    if current_path is None:
        # Resolve current path
        current_path = cmds.file(q=True, sceneName=True)
        if not current_path:
            pymel.warning("Please save your scene!")
            return

    current_path_dirname = os.path.dirname(current_path)
    current_path_basename = os.path.basename(current_path)
    current_path_filename, current_path_fileext = os.path.splitext(current_path_basename)
    return os.path.join(current_path_dirname, '{0}{1}'.format(current_path_filename, current_path_fileext)) 



## get_default_path_snapshot()
