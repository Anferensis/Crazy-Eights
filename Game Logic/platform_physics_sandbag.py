
"""
Written by Albert"Anferensis"Ong

Controls platform physics for a sandbag.
"""

from bge import logic

def main():

    cont = logic.getCurrentController()
    scene = logic.getCurrentScene()
    
    own = cont.owner
    near = cont.sensors["Platform Physics"]
    
    if near.positive:
        
        for object in near.hitObjectList:
            if own.worldPosition.z > (object.worldPosition.z+.5):
                scene.addObject("Collision Platform",object,1)
                

   



#===================================================

main()


