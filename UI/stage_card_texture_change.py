
"""
Written by Albert "Anferensis" Ong
"""

import os
from bge import logic, texture


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    message = owner.sensors["Message"]
    
    if message.positive:
        
        subject = message.subjects[0]
        
        
        matID = texture.materialID(owner, "MA" + "Stage Card")  
        tex = texture.Texture(owner, matID, 0)
        
        cwd = logic.expandPath("//")
        os.chdir(cwd)
        os.chdir("../../2D Art Files/UI Textures/Stage Card Textures")
           
        texture_path_dict = {
        
            "-2" : "/Rock_Concert_card.png",
            "-1" : "/game_test_card.png",
             "0" : "/random_stage_card.png",
             "1" : "/Belair_Estate_card.png",
             "2" : "/Sunset_Pier_card.png", }
             
        texture_path = texture_path_dict[subject]
            
        new_cwd = os.getcwd()
        image_path = new_cwd + texture_path   
        tex.source = texture.ImageFFmpeg(image_path)

        owner["texture_property"] = tex
        tex.refresh(True)

 

#======================================================

main()


