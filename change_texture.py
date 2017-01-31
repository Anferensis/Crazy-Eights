
"""
Written by Albert "Anferensis" Ong

Changes the texture of a material.
"""

from bge import logic, texture


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    # Insert name of material.
    mat_name = ""
   
    matID = texture.materialID(owner, "MA" + mat_name)  
    tex = texture.Texture(owner, matID, 0)
    
    # Insert path to new image.
    image_path = ""
    
    url = logic.expandPath("//" + image_path)
    tex.source = texture.ImageFFmpeg(url)

    owner["texture_property"] = tex
    tex.refresh(True)



#======================================================

main()


