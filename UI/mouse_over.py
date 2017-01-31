
"""
Written by Albert "Anferensis" Ong

Controls mouse over visual effects
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    mouse_over = cont.sensors["Mouse Over"]
    
    if mouse_over.positive:
        owner.visible = True
        
    else:
        owner.visible = False



#======================================================

main()


