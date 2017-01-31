
"""
Written by Albert "Anferensis" Ong
"""

from random import randint
from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    primary = owner.sensors["Primary"]
    delay = owner.sensors["Delay"]
    
    if primary.positive:
        owner["Stage Selected"] = True
        cont.activate("Loading Screen")
        
        main_scene = logic.getSceneList()[1]
        main_scene_objects = main_scene.objects
        main_properties = main_scene_objects["Main Properties"]
        main_properties["Loading Game"] = 1
        
        
    if owner["Stage Selected"] and delay.positive:
              
        current_stage = owner["Current Stage"]
        
        if current_stage == "RANDOM":
            
            random_stage_num = randint(0, 3)
            print(random_stage_num)
            
            stage_num_dict = {
            
                0 : "ROCK CONCERT", 
                1 : "GAME TEST", 
                2 : "BELAIR ESTATE", 
                3 : "SUNSET PIER", }
                
            stage_name = stage_num_dict[random_stage_num]
            
            cont.activate(stage_name)
                       
        else:           
            cont.activate(current_stage)



#======================================================

main()


