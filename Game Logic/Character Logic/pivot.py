
"""
Written by Albert "Anferensis" Ong

Controls character facing and pivoting.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    left_tap = owner.sensors["Left Tap"]
    right_tap = owner.sensors["Right Tap"]
    facing = owner["Facing"]
    
    if left_tap.positive and facing == "Right":
        cont.activate("Left Pivot")
        owner["Facing"] = "Left"
    
    elif right_tap.positive and facing == "Left":
        cont.activate("Right Pivot")
        owner["Facing"] = "Right"
         
    else:
        cont.deactivate("Left Pivot")
        cont.deactivate("Right Pivot")
    


#======================================================

main()


