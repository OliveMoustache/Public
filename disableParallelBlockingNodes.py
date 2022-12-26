# Original script by Chris Lesage,
# shared on https://discourse.techart.online/t/parallel-evaluation-wisdom/10340
# Thanks Chris 

# Start of the script
# Find the nodetype that are blocking parallel evaluation. Then disable parallel evaluation on each of those 
import pymel.core as pm
import maya.mel as mel

blockingNodes = mel.eval('evaluator -name "dynamics" -valueName "disabledNodes" -query;')
# This returns strings for MEL later. Needs to be Pythonified and de-MELLED.
blockingTypes = [str(pm.PyNode(x).type()) for x in str(blockingNodes).split('\n') if x]
print(blockingTypes)

for eachType in blockingTypes:
    mel.eval('evaluator -name dynamics -c "disablingNodes=none";')
    mel.eval('evaluator -name dynamics -c "handledNodes={}";'.format(eachType))
    mel.eval('evaluator -name dynamics -c "action=evaluate";')

print("//////////// Blocking nodes disabled /////////////")
