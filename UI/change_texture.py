
"""
Written by Albert "Anferensis" Ong

Changes the texture of a material on mouse over.
"""

import os
from bge import logic
from bge import texture


def main():
    
    cont = logic.getCurrentController()
    owner= cont.owner
 
    # Insert material name
    material_name = "Stock Mode Button"
    
    matID = texture.materialID(owner, "MA" + material_name)  
    tex = texture.Texture(owner, matID, 0)
    

    click = cont.sensors["Click"]
    mouse_over = cont.sensors["Mouse Over"]
    
    if click.positive and mouse_over.positive:
        
        objects = logic.getCurrentScene().objects
        props = objects["Properties"]
        stock_mode = props["Stock Mode"]
        
        
        if stock_mode == "Stock All":
            new_stock_mode = "Stock Pick"
            image_path = "stock_pick.png"
            
        else:
            new_stock_mode = "Stock All"
            image_path = "stock_all.png"
        
                               
        props["Stock Mode"] = new_stock_mode     
        
        os.chdir(logic.expandPath("//"))
        tex.source = texture.ImageFFmpeg(image_path)

        owner["texture_property"] = tex
        tex.refresh(True)



#======================================================

main()


