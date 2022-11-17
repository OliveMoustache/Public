// simple command to save and reselect your current selection 
// after launching TweenMachine

ctlSel = cmds.ls( selection=True )
mel.eval('tweenMachine()')
cmds.select ( ctlSel )
