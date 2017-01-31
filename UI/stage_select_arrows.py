
"""
Written by Albert "Anferensis" Ong
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    click = owner.sensors["Click"] 
    mouse_over = owner.sensors["Mouse Over"]
    
    
    if click.positive and mouse_over.positive:
        
        direction = owner["Direction"]
        owner.sendMessage(direction, "", "Stage Cards")
        



#======================================================

main()


