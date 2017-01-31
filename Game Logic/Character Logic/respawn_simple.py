
"""
Written by Albert"Anferensis"Ong

A simplefied respawn script.
Used for early functionality testing.
"""

from bge import logic


def main():

    cont = logic.getCurrentController()
    owner = cont.owner
    
    collision = owner.sensors["Blast Zones"]
    
    if collision.positive:
        
        cont.activate("KO")

        objects = logic.getCurrentScene().objects
        stage_props = objects["Stage Properties"]
        
        spawn_x = stage_props["Spawn_X"]
        spawn_z = stage_props["Spawn_Z"]
        
        owner.position.x = spawn_x
        owner.position.z = spawn_z
    
    
    
#================================================
    
main()


