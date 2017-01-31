
"""
Written by Albert"Anferensis"Ong

Plays a movie texture.
"""

from bge import logic
from bge import texture

def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner

    if "Video" in owner:
    	
    	video = owner["Video"]
    	video.refresh(True)
					
    else:
        
        #Insert material name.
        mat = "Movie"
        
        matID = texture.materialID(owner, "MA" + mat)
        video = texture.Texture(owner, matID)
        owner["Video"] = video
        
        #Insert path to movie file.
        movie_path = ""
        
        path = logic.expandPath('//' + movie_path)
        video.source = texture.VideoFFmpeg(path)
        
        video.source.play()
    
#===============================================================

main()


