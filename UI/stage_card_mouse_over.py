
"""
Written by Albert "Anferensis" Ong

Changes the image of the stage card.
"""

import os
from bge import logic
from bge import texture


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    mouse_over = cont.sensors["Mouse Over"]
    
    if mouse_over.positive:
        
        name = owner.name[:-7]
 
        if name == "Stage1":
            image_name = "/game_test_card.png" 
            
        elif name == "Stage2":
            image_name = "/Rock_Concert_card.png" 
            
        elif name == "Stage3":
            image_name = "/Belair_Estate_card.png" 
            
        elif name == "Stage4":
            image_name = "/Sunset_Pier_card.png"    
              
    else:
        image_name = "/no_stage_card.png"
        
        
    objects = logic.getCurrentScene().objects
    stage_card = objects["Stage Card"]
   
    matID = texture.materialID(stage_card, "MA" + "Stage Card")  
    tex = texture.Texture(stage_card, matID, 0)
    
    # Specifying the path to the image.
    cwd = logic.expandPath("//")
    os.chdir(cwd)
    os.chdir("../../2D Art Files/PNG/UI PNG/Stage Cards PNG")
    new_cwd = os.getcwd()
    
    image_path = new_cwd + image_name
    tex.source = texture.ImageFFmpeg(image_path)

    owner["texture_property"] = tex
    tex.refresh(True)



#======================================================

main()


