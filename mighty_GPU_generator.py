/*
//  Mighty Tail world switcher v2.3
//  mighty_tail_world_switcher.mel
// by Olivier Ladeuix
//

// This script is to create a world control for the tail on the fly
// The name will reflect the character's name ie. mighty_TWS_Loudo_FK_CTRL 
// which will be located under __TRASH__> mighty_TWS_Loudo_locator_B

/////////// How to install  //////////////////////
// Place the script in your scripts folder
// Do a rehash or restart Maya for Maya to load the script

/////////// How to use  //////////////////////
//
// 1. Ideally you want to orient the main and placement controls to the world before starting the script
//        just so the new control is align to the world in default pose. 
// 2. Select the control you want to add a world control to. Usually something like Rosie:FKTail01_M_CTRL
// 3. Run the script with the following command: 
// You can launch the script through a button on the shelf using the following code :
// source "mighty_tail_world_switcher"; mighty_tail_world_switch();
//            You could also use a hotkey
// 4. To delete the system, delete the following items :
//           mighty_tail_world_switch_locator_A and mighty_tail_world_switch_locator_B  
//
////////////////////////////////

////////

CHANGELOG:
2021 06 27    v1.0 
2021 06 29    v2.0 added the namespace to the locator and constraints names.
2021 06 29    v2.1 renamed the locator to include the character's name
2021 07 27    v2.2 Modified the "How to use" section and now parenting the locator under the __TRASH__ folder
2021 07 28    v2.3 Modified the "How to use" section



*/

/// FAQ
/// If you get an error message saying "// Error: line 54: No object matches name: "
///         This is because you didn't select the tail FK control
////////////////////////////////


global proc mighty_tail_world_switch() {    

// Make a variable from the selection 
string $mighty_World_switch_selection[] = `ls -sl`;
print ("Object selected is : " + $mighty_World_switch_selection[0]);

// Get character's Namespace
string $charName[];
$numTokens = `tokenize $mighty_World_switch_selection[0] ":" $charName`;
// $charName[0] is now our namespace

// Creation of locator A as a variable
$mighty_TWS_loc_A = ("mighty_TWS_" + $charName[0] + "_locator_A");
spaceLocator -name $mighty_TWS_loc_A ;

// Snap locator to the first tail FK chain through a constraint then delete the constraint and duplicate Loc A to Loc B
parentConstraint -name CONST_TEMP_mighty_tail_world_switch $mighty_World_switch_selection[0] $mighty_TWS_loc_A ;
delete CONST_TEMP_mighty_tail_world_switch;

// Creation of locator B and pointConstraint to A
$mighty_TWS_loc_B = ("mighty_TWS_" + $charName[0] + "_locator_B");
duplicate -name $mighty_TWS_loc_B $mighty_TWS_loc_A;
pointConstraint -name ("mighty_TWS_" + $charName[0] + "_ConstPoint_to_Loc_A") $mighty_TWS_loc_A $mighty_TWS_loc_B;

// Create our new FK World control as a variable
$mighty_TWS_FK_CTRL = ("mighty_TWS_" + $charName[0] + "_FK_CTRL");
print ("//// Our new tail control is called : " + $mighty_TWS_FK_CTRL + " /////////" );
circle -n ("mighty_TWS_" + $charName[0] + "_FK_CTRL") -c 0 0 0 -nr 0 0 1 -sw 360 -r 8 -d 8 -ut 0 -tol 0.01 -s 8 -ch 0;
setAttr ($mighty_TWS_FK_CTRL + ".overrideEnabled") 1;
setAttr ($mighty_TWS_FK_CTRL + ".overrideColor") 4;
setAttr ($mighty_TWS_FK_CTRL + ".rotateOrder") 2;

// Align to loc_B
pointConstraint -name mighty_TWS_Const_TEMP $mighty_TWS_loc_B $mighty_TWS_FK_CTRL ;
delete mighty_TWS_Const_TEMP;
parent $mighty_TWS_FK_CTRL $mighty_TWS_loc_B ;
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;

// creation of the constraint from Locator A to FKRoot or hips
parentConstraint -mo -weight 1 -name ("mighty_TWS_" + $charName[0] + "_Const_to_Root") ($charName[0] + ":FKRoot_M_CTRL") $mighty_TWS_loc_A ;

// creation of the constraint from FKTail top control to mighty_TWS_FK_CTRL
parentConstraint -weight 1 -name ("mighty_TWS_" + $charName[0] + "_Const_to_TWS_FK_CTRL") $mighty_TWS_FK_CTRL $mighty_World_switch_selection[0] ;

// parenting the locator under the __TRASH__ folder
parent $mighty_TWS_loc_A __TRASH__ ;
parent $mighty_TWS_loc_B __TRASH__ ;

// Done
print ("/////// Mighty Tail World switch control created for " + $charName[0] + " ///////// ");

}


