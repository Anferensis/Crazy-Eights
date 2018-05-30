
"""
Written by Albert "Anferensis" Ong

Controls a texture that follows the mouse's location.

This effect is purely aesthetic and is designed to give the illusion
that the visual representation of the mouse has been altered.  

Revision: 05-29-2018 
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    # Looks for a sensor named Mouse.
    # This sensor activates on every frame and responds to
    # any mouse over input. 
    mouse = cont.sensors["Mouse"]
    
    # Retrieves the position of the mouse. 
    hit_position = mouse.hitPosition
    
    # Changes the position of the texture to the mouse's location. 
    owner.position.x = hit_position.x
    owner.position.y = hit_position.y

    # This code block will activate on every frame and give the 
    # illusion that the texture is the mouse. 
    

#======================================================

main()


