
"""
Written by Albert "Anferensis" Ong

Controls attacking logic for a character.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    viable_attacks = ("Neutral", "Up Neutral", "Down Neutral", "Forward Neutral",
                      "Up Jazz", "Down Jazz", "Forward Jazz",
                      "Neutral Aerial", "Up Aerial", "Down Aerial", 
                      "Forward Aerial", "Back Aerial", )
                      
    
    message  = owner.sensors["Message"]
    
    if message.positive:
        
        action_name = message.subjects[0]
        
        if action_name in viable_attacks:        
            
            owner["attack_data"] = owner["frame_data"][action_name] 
            owner["inAction"] = True
            owner["isAttacking"] = True
        
        
    if owner["inAction"]:
        
        attack_data = owner["attack_data"] 
        phases = attack_data["phases"]
        
        for phase_name in phases:
            
            phase_data = attack_data[phase_name]
            
            active_frames = phase_data["active_frames"]
            current_frame = owner["Frame"]
            
            if current_frame in active_frames:
                
                hitboxes = phase_data["hitboxes"]
                
                for hitbox_num in hitboxes:
                    
                    hitbox_name = " ".join(["Wedge", "Hitbox", hitbox_num])
                    owner.sendMessage("Active!", "", hitbox_name)
    
    
              
    if owner["isAttacking"]:       
         
        attack_data = owner["attack_data"]          
        phases = attack_data["phases"]
               
        for phase_name in phases:
            
            phase_data = attack_data[phase_name]
            
            active_frames = phase_data["active_frames"]
            current_frame = owner["Frame"]
            
            
            if current_frame in active_frames:
                           
                hitboxes = phase_data["hitboxes"]
                
                for hitbox_num in hitboxes:
                    
                    hit = False
                    
                    children = owner.children
                    
                    hitbox_name = " ".join(["Wedge", "Hitbox", hitbox_num])
                    hitbox = children[hitbox_name]
                                       
                    hitbox_data_name = "_".join(["hitbox", "data", hitbox_num])
                    hitbox_data = phase_data[hitbox_data_name]
                    
                    hit_detection = hitbox.sensors["Hit Detection"]
                    hit_objects = list(hit_detection.hitObjectList)
                    
                    
                    for obj in hit_objects:   
                        
                        if obj != owner.parent:
                        
                            damage = hitbox_data["damage"]
                            obj["Percent"] += damage
                            
                            
                            force_x = hitbox_data["force_x"]
                            force_z = hitbox_data["force_z"]                                                                                                            
                            scaling = hitbox_data["scaling"]
                            percent = obj["Percent"]
                            
                            force_x = force_x * scaling * percent
                            force_z = force_z * scaling * percent 
                            
                            if owner["Facing"] == "Left":
                                force_x *= -1                       
                            
                            obj.linearVelocity = [force_x, 0.0, force_z]
                            
                            
                            percent_str = str(obj["Percent"])
                            percent_len = len(percent_str)
                            
                            spacing_dict = { 1 : "    ",
                                             2 : "  ",
                                             3 : ""}                                     
                            spacing = spacing_dict[percent_len]
                            
                            text = spacing + percent_str
                            overlay = logic.getSceneList()[1]
                            percent_text = overlay.objects["P2 Percent"]
                            
                            percent_text.text = text
                            
                            owner.sendMessage(str(damage), "", "P2 Percent") 
                              
                            hit = True 
                            
                    if hit:
                        break                   
                                    
                if hit:
                    owner["isAttacking"] = False
                    break  
    
    
    
    action_name = owner.getActionName()
                                     
    if action_name in ("Idle", ""):
        
        owner["inAction"] = False
        owner["isAttacking"] = False                            


                                                                                                                              
#======================================================

main()


