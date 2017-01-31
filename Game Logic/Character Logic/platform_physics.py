
"""
Written by Albert"Anferensis"Ong

Controls platform physics for a character.
"""

from bge import logic


def main():

    cont = logic.getCurrentController()
    owner = cont.owner
    
    platform_detection = cont.sensors["Platform Detection"]
    down = cont.sensors["Down"]
    
        
    if platform_detection.positive and not down.positive:                  
        
        platform = platform_detection.hitObject
        owner["last_platform"] = platform        
        platform.collisionGroup = 1
            
    else:
        owner["last_platform"].collisionGroup = 2
        
    
                                         
#===================================================

main()


