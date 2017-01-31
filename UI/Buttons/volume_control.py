
"""
Written by Albert "Anferensis" Ong

Controls the game volume.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    objects = logic.getCurrentScene().objects
    
    click = cont.sensors["Click"]
    mouse_over = cont.sensors["Mouse Over"]
    
    
    if click.positive and mouse_over.positive:
        
        volume = logic.globalDict["Volume"]
        text = objects["Sound Number Text"]
        
        
        if volume == 1.0:
            new_volume = 0.0
                
        elif volume == 0.0:
            new_volume = 1.0
            
            
        text.text = str(new_volume)
        logic.globalDict["Volume"] = new_volume
            
            
        cont.activate("Volume")
            
    

#======================================================

main()


