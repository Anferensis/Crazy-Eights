
"""
Written by Albert"Anferensis"Ong

Draws a ray sensor.
"""

from bge import logic, render

def main():

    cont = logic.getCurrentController()
    owner = cont.owner
    
    ray = cont.sensors["Ray"]
    
    if ray.positive:
        render.drawLine(owner.worldPosition, ray.hitPosition, [1,0,0])
   


#==================================================

main()



