
"""
Written by Albert "Anferensis" Ong

Controls mouse icon movement.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    mouse = cont.sensors["Movement"]
    
    hit_position = mouse.hitPosition
    
    owner.position.x = hit_position.x
    owner.position.y = hit_position.y



#======================================================

main()


