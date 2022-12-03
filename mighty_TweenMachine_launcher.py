""" 
mighty_TweenMachine_launcher.py is a simple trick to
launch TweenMachine without losing your current controls' selection.

All steps are described for those who want to customise or tweak the script 
    and learn from it.

You might just have to customise the paragraph in line 21 and 22
    depending on how you launch TweenMachine.
"""

## Start of the script and import of the Maya commands as cmds
import maya.cmds as cmds

## The following line saves your current selection as a variable called ctlSel using the ls command
ctlSel = cmds.ls( selection=True )

## The following paragraph is the default command to launch Tween machine. 
## Just copy and paste the current command on your system

## I am using Justin Barret's tweenmachine.py 3.0.0
## https://github.com/boredstiff/tweenMachine
## so for me it is as follows
 
import tweenMachine
tweenMachine.start()

## Now that we have launched Tween Machine, we simply reselect 
## our controls using the ctlSel variable

cmds.select ( ctlSel )


## That's it, thanks Justin Barrett and contributors for this 
## simple but most useful tool.
