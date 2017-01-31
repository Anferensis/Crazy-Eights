
"""
Written by Albert "Anferensis" Ong

Changes the color of an object.
"""

from bge import logic


def main():

    cont = logic.getCurrentController()
    owner = cont.owner
    
    spacebar = owner.sensors["Spacebar"]
    
    if spacebar.positive:
        new_color = [1.0, 0.0, 0.0, 0.5]
        
    else:
        new_color = [0.0, 0.0, 1.0, 0.5]
        
    owner.color = new_color



#====================================================

main()


