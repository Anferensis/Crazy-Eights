
"""
Written by Albert "Anferensis" Ong

Controls hitstun and knockback logic.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    
    hit = owner.sensors["Hit"]
    
    if hit.positive:
        
        forces = [float(body) for body in hit.bodies]
        
        force_x = forces[0]
        force_z = forces[1]
        
        knockback = owner.actuators["Knockback"]
        knockback.dLoc = [force_x, 0.0, force_z]
        cont.activate(knockback)
    
    
    else:
        cont.deactivate("Knockback")
        
        
    
#======================================================

main()


