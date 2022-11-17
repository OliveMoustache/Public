ctlSel = cmds.ls( selection=True )
mel.eval('tweenMachine()')
cmds.select ( ctlSel )
