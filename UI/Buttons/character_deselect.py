
"""
Written by Albert "Anferensis" Ong
"""

import os
from bge import logic
from bge import texture


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    secondary = owner.sensors["Secondary"]
    
    if secondary.positive and owner["Character Selected"]:
        owner["Character Selected"] = False
        
        objects = logic.getCurrentScene().objects
        
        select_character_text = objects["Select Character Text"]
        select_character_text.text = "SELECT CHARACTER"
        
        
        character_portrait_glow = objects["Character Portrait Glow"]
        character_portrait_glow.visible = False
        
        
        character_portrait = objects["Character Portrait"]
        matID = texture.materialID(character_portrait, "MA" + "Character Portrait")  
        tex = texture.Texture(character_portrait, matID, 0)
        
        # Specify path to image.
        os.chdir(logic.expandPath("//"))
        os.chdir("../Rendered Images/Character Portraits")
        cwd = os.getcwd()
        
        image_path = cwd + "/black.png"
        tex.source = texture.ImageFFmpeg(image_path)

        owner["texture_property"] = tex
        tex.refresh(True)



#======================================================

main()


