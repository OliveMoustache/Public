### mighty_lightAligner.py
### v1.0
#### Olivier Ladeuix

#### Start the script, select the light you want to align
#### Select the face you want to align (F8), the geometry needs to be selectable
#### Hit Align Spec or Align Shadow depending whenre you want the selected face to be.


import maya.cmds as cmds
import maya.api.OpenMaya as om

stored_light = None  # Remember chosen light

def set_light(*args):
    """Store the currently selected light."""
    global stored_light
    sel = cmds.ls(selection=True, type='transform')
    if not sel:
        cmds.warning("Please select a light.")
        return
    
    for obj in sel:
        shapes = cmds.listRelatives(obj, shapes=True) or []
        for s in shapes:
            if cmds.nodeType(s) in ['ambientLight', 'directionalLight', 'pointLight', 'spotLight', 'areaLight', 
            'volumeLight', 'aiAreaLight', 'aiPhotometricLight' ]:  
                stored_light = obj
                cmds.text('lightLabel', edit=True, label=f"Selected Light: {stored_light}")
                cmds.inViewMessage(amg=f"{stored_light} is Active", pos='midCenter', fade=True)
                return
    
    cmds.warning("Selected object is not a light.")

def align_light(opposite=True):
    """Align the stored light to face normal or opposite, keeping face selected."""
    global stored_light
    if not stored_light:
        cmds.warning("No light stored. Click 'Set Light' first.")
        return

    # Save current selection (so we can restore it later)
    saved_selection = cmds.ls(selection=True)

    sel = om.MGlobal.getActiveSelectionList()
    if sel.length() == 0:
        cmds.warning("Please select a face on a mesh.")
        return

    dagPath, comp = sel.getComponent(0)
    if not comp or comp.apiTypeStr != 'kMeshPolygonComponent':
        cmds.warning("Please select a face, not an object.")
        return

    meshFn = om.MFnMesh(dagPath)
    faceIt = om.MItMeshPolygon(dagPath, comp)
    faceIndex = faceIt.index()

    center = faceIt.center(om.MSpace.kWorld)
    normal = meshFn.getPolygonNormal(faceIndex, om.MSpace.kWorld)

    offset_distance = 10.0
    if opposite:
        # Offset along opposite normal
        light_pos = (
            center.x - normal.x * offset_distance,
            center.y - normal.y * offset_distance,
            center.z - normal.z * offset_distance
        )
        target_pos = (center.x - normal.x, center.y - normal.y, center.z - normal.z)
        aim_message = f"Shadow side"
    else:
        # Offset along same normal
        light_pos = (
            center.x + normal.x * offset_distance,
            center.y + normal.y * offset_distance,
            center.z + normal.z * offset_distance
        )
        target_pos = (center.x + normal.x, center.y + normal.y, center.z + normal.z)
        aim_message = f"Specular side"

    # Create temp aim target
    aim_target = cmds.spaceLocator(name="aim_target_temp")[0]
    cmds.xform(aim_target, ws=True, t=target_pos)

    # Move light to offset position
    cmds.xform(stored_light, ws=True, t=light_pos)

    # Aim constraint
    cmds.aimConstraint(aim_target, stored_light, aimVector=(0,0,-1))

    # Delete temp locator
    cmds.delete(aim_target)

    # Restore previous selection
    if saved_selection:
        cmds.select(saved_selection, replace=True)

    cmds.inViewMessage(amg=aim_message, pos='midCenter', fade=True)

def align_light_opposite(*args):
    align_light(opposite=True)

def align_light_same(*args):
    align_light(opposite=False)

def create_ui():
    """Create the UI window."""
    if cmds.window('lightAlignWin', exists=True):
        cmds.deleteUI('lightAlignWin')

    cmds.window('lightAlignWin', title='Align Light to Face Normal',tlc = (100,90), widthHeight=(300,250), menuBar=True, sizeable=False)
    cmds.columnLayout(adjustableColumn=True, columnAttach=('both', 5), rowSpacing=10)

    cmds.separator(height=10) 
    cmds.text('lightLabel', label="Selected Light: None")
    cmds.button(label="Set Light from Selection", command=set_light)
    cmds.separator(height=15, style='in')
    cmds.text(label="Select a face, then choose alignment:")
    cmds.button(label="Align Spec", height=40, command=align_light_same, bgc=(1, 1, 1) )
    cmds.button(label="Align Shadow", height=40, command=align_light_opposite )

    cmds.setParent('..')
    cmds.showWindow('lightAlignWin')

# Run UI
create_ui()
