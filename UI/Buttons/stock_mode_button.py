
"""
Written by Albert "Anferensis" Ong

Changes the texture of the stock mode button when clicked.
"""

import os
from bge import logic
from bge import texture


def main():
    
    cont = logic.getCurrentController()
    owner= cont.owner
 
    # Insert material name.
    material_name = "Stock Mode Button"
    
    matID = texture.materialID(owner, "MA" + material_name)  
    tex = texture.Texture(owner, matID, 0)
    

    click = cont.sensors["Click"]
    mouse_over = cont.sensors["Mouse Over"]
    
    if click.positive and mouse_over.positive:
        
        objects = logic.getCurrentScene().objects
        properties = objects["Character Select Properties"]
        stock_mode = properties["Stock Mode"]
        
        
        if stock_mode == "Stock All":
            new_stock_mode = "Stock Pick"
            image_path = "stock_pick.png"
            
        else:
            new_stock_mode = "Stock All"
            image_path = "stock_all.png"
        
                               
        properties["Stock Mode"] = new_stock_mode     
        
        cwd = logic.expandPath("//")
        os.chdir(cwd)
        
        path_extension = "../../2D Art Files/PNG/UI PNG/"
        os.chdir(path_extension)
        
        # Applies and refreshes the new texture.
        tex.source = texture.ImageFFmpeg(image_path)
        owner["texture_property"] = tex
        tex.refresh(True)



#======================================================

main()


