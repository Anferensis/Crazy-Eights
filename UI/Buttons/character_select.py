
"""
Written by Albert "Anferensis" Ong

Controls character selection visual effects and logic.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    objects = logic.getCurrentScene().objects
    properties = objects["Character Select Properties"]
    
    
    if not properties["Character Selected"]:
    
        click = owner.sensors["Click"]
        mouse_over = owner.sensors["Mouse Over"]
        
        
        if click.positive and mouse_over.positive:
                 
            name_dict = { "Random Character" : "Random" , 
                          "Character1"       : "Cube" ,
                          "Character2"       : "Figurine"}
                          
            obj_name = owner.name[:-7]             
            char_name = name_dict[obj_name]
               
               
            select_character_text = objects["Select Character Text"]
            select_character_text.text = char_name
            
            owner.visible = False
            logic.globalDict["Player 1"] = char_name
            properties["Character Selected"] = True
            
            cont.activate("Select Sound")

        

#======================================================

main()


