
"""
Written by Albert"Anferensis"Ong

Controls the respawn of a character.
This script is activated when a character contacts the blast zones.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    player_num = str(owner["player_num"])
    stock_num = str(owner["Stocks"])
   
    delay = owner.sensors["Respawn Delay"]
    collision = owner.sensors["Blast Zone"]
    
    if collision.positive:
        owner["Dead"] = True
        
        
    if owner["Dead"]:
        
        if owner["Stocks"] == 1:
            
            ko_sound = owner.actuators["KO"]
            ko_sound.startSound()
            
            overlay_objects = logic.getSceneList()[1].objects
            stock_name = "P" + player_num + " Stock" + stock_num
            overlay_objects[stock_name].visible = False
            
            scene = logic.getCurrentScene()
            stage_props = scene.objects["Stage Properties"]
            stage_props["Game Over"] = True
        
        
        elif delay.positive:
            
            owner["Stocks"] -= 1
            
            # Spawn locations are stored in the stage properties.
            objects = logic.getCurrentScene().objects
            stage_props = objects["Stage Properties"]
            
            # Spawn location differs based on the player number.
            spawn_x = "Spawn_" + player_num + "X"
            spawn_z = "Spawn_" + player_num + "Z"
            
            owner.position.x = stage_props[spawn_x]
            owner.position.z = stage_props[spawn_z]
            
            owner["Dead"] = False
            
            
        else:
            
            ko_sound = owner.actuators["KO"]
            ko_sound.startSound()
            
            # Makes the stock icon in the overlay invisible.
            overlay_objects = logic.getSceneList()[1].objects
            stock_name = "P" + player_num + " Stock" + stock_num
            overlay_objects[stock_name].visible = False
            
          
            
            

        
    
#==================================================
    
main()



