
"""
Written by Albert "Anferensis" Ong

Controls logic for shielding and shield breaking.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    shield = cont.sensors["Shield"]
    
    # Checks if the size of the shield is above its minimum size
    # and below its maximum size.
    scaling = list(owner.scaling)
    scaling_above_min = all([num > 0.25 for num in scaling]) 
    scaling_below_max = all([num < 1.00 for num in scaling])
    
    
    # Shield breaks if it is too small.
    if not scaling_above_min:
        owner["Shield Break"] = True
        cont.activate("Shield Break Sound")
        
   
    not_shield_break = not owner["Shield Break"]    
    
    # Shield shrinks when pressing the shield button.
    if shield.positive and scaling_above_min and not_shield_break:        
        visibility = True
        owner["Shield Health"] -= 1.0        
        add_scaling = -0.0025   
    
    
    # Shield regeneration when not in use.         
    elif scaling_below_max and not_shield_break:         
        visibility = False
        owner["Shield Health"] += 0.5       
        add_scaling = 0.00125   
    
    
    # Shield regeneration after shield break.
    elif owner["Shield Break"]:        
        visibility = False
        owner["Shield Health"] += 2.0
        add_scaling = 0.005
 
    
    # Otherwise
    else:
        visibility = False
        add_scaling = 0.0   
       
       
    # Applies scaling and visibility to owner.
    owner.visible = visibility          
    new_scaling = [num + add_scaling for num in scaling]
    owner.scaling = new_scaling 
    
    
    # Resets shield break when shield is fully regenerated.
    if owner["Shield Health"] >= 300.0 and owner["Shield Break"]:
        owner["Shield Break"] = False 
        


#======================================================

main()


