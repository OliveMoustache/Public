### mighty_Fix_light.py
### by Olivier Ladeuix
## v1.0

## This script is to quickly create an area light in your scene to troubleshoot displacement issues
## 
## How to use:
##    Select an object then launch the script
##        From the UI you can either snap a light to the selected control
##        or point constraint a light to this object.


import maya.cmds as cmds

# ----------------------------------------------------------
# Main light creation logic (reusable function)
# ----------------------------------------------------------
def create_arnold_light(point_constrain=False):
    sel = cmds.ls(selection=True)
    if not sel:
        cmds.error("Please select an object to snap the area light to.")
        return
    target = sel[0]

    # Create Arnold area light
    ai_area_light = cmds.shadingNode('aiAreaLight', asLight=True)
    cmds.setAttr(ai_area_light + '.exposure', 11)

    # Rename transform
    ai_area_light = cmds.rename(ai_area_light, 'Fix_areaLight')

    # Rotate order
    cmds.setAttr(ai_area_light + '.rotateOrder', 3)

    # Offset pivot
    cmds.xform(ai_area_light, pivots=(0, 0, -10), worldSpace=False)

    # Snap to target (position + rotation)
    cmds.delete(cmds.pointConstraint(target, ai_area_light))
    cmds.delete(cmds.orientConstraint(target, ai_area_light))

    # Optional: keep it constrained dynamically
    if point_constrain:
        cmds.pointConstraint(target, ai_area_light, mo=True)
        print("Point constraint added between", ai_area_light, "and", target)

    # Set render resolution (1080p)
    cmds.setAttr("defaultResolution.width", 1920)
    cmds.setAttr("defaultResolution.height", 1080)
    cmds.setAttr("defaultResolution.deviceAspectRatio", 1920.0/1080.0)
    cmds.setAttr("defaultResolution.pixelAspect", 1.0)

    # Arnold render sampling
    cmds.setAttr("defaultArnoldRenderOptions.AASamples", 3)
    cmds.setAttr("defaultArnoldRenderOptions.GIDiffuseSamples", 2)
    cmds.setAttr("defaultArnoldRenderOptions.GISpecularSamples", 1)
    cmds.setAttr("defaultArnoldRenderOptions.GITransmissionSamples", 0)
    cmds.setAttr("defaultArnoldRenderOptions.GISssSamples", 0)
    cmds.setAttr("defaultArnoldRenderOptions.GIVolumeSamples", 0)
    cmds.setAttr("defaultArnoldRenderOptions.enableProgressiveRender", 1)

    print("Created and configured Arnold light:", ai_area_light)
    # Save reference to the last created light
    _last_created_light = ai_area_light



# ----------------------------------------------------------
# Delete the last created light
# ----------------------------------------------------------
def delete_last_light(*_):
    global _last_created_light
    if _last_created_light and cmds.objExists(_last_created_light):
        cmds.delete(_last_created_light)
        print("Deleted last created light:", _last_created_light)
        _last_created_light = None
    else:
        cmds.warning("No recently created light found or it's already deleted.")





# ----------------------------------------------------------
# UI Function
# ----------------------------------------------------------
def open_light_ui():
    # If UI already exists, delete it
    if cmds.window("lightToolWin", exists=True):
        cmds.deleteUI("lightToolWin")

    # Create window
    window = cmds.window("lightToolWin", title="mighty_Fix_light", widthHeight=(120, 80))
    cmds.columnLayout(adjustableColumn=True, rowSpacing=10)

    cmds.text(label="Fix Light Creation Tool", align='center', height=25)


    cmds.button(label="Snap Light",
                bgc=(1.0, 1.0, 0.3),
                command=lambda *_: create_arnold_light(point_constrain=False))


    cmds.button(label="Snap + Point Constrain Light",
                bgc=(1.0, 0.6, 0.2),
                command=lambda *_: create_arnold_light(point_constrain=True))

#    cmds.separator(height=10, style='in')
#    cmds.button(label="Delete Last Created Light",
#                bgc=(0.8, 0.3, 0.3),
#                command=delete_last_light)


    cmds.showWindow(window)


# ----------------------------------------------------------
# Run the UI
# ----------------------------------------------------------
open_light_ui()


