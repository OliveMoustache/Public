import maya.cmds as cmds
lamberts = cmds.ls(type='lambert')
for lambert in lamberts:
    cmds.setAttr('{}.ambientColor'.format(lambert), 0, 0, 0)
    cmds.setAttr('{}.diffuse'.format(lambert), 1)
