
"""
Written by Albert "Anferensis" Ong

Controls attacking logic for a character.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    
    message = owner.sensors["Message"]
       
    if message.positive:
        
        action_name = message.subjects[0]
               
        owner["attack_data"] = owner["frame_data"][action_name]
               
        owner["isAttacking"] = True
        owner["inAction"] = True
    
   
    
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
                
                    children = owner.children
                    
                    hitbox_data_name = "_".join(["hitbox", "data", hitbox_num])
                    hitbox_data = phase_data[hitbox_data_name]
                    
                    hitbox_color = hitbox_data["color"]
                        
                    hitbox_name = " ".join(["Wedge", "Hitbox", hitbox_num])
                    hitbox = children[hitbox_name]
                    
                    owner.sendMessage(hitbox_color, "", hitbox_name)         
           
    
    
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
                        damage = hitbox_data["damage"]
                        obj["Percent"] += damage
                        
                        
                        force_x = hitbox_data["force_x"]
                        force_z = hitbox_data["force_z"]                                                                                                            
                        scaling = hitbox_data["scaling"]
                        percent = obj["Percent"]
                        
                        force_x = force_x * scaling * percent
                        force_z = force_z * scaling * percent 
                        
                        force_total = [force_x, 0.0, force_z]
                        
                        obj.linearVelocity = force_total
                        
                        hit = True
                    
                        
                    if hit:
                        owner["isAttacking"] = False
                        break
    
    
                         
    action_name = owner.getActionName()
        
    if action_name in ("Idle", ""):
        owner["isAttacking"] = False
        owner["inAction"] = False
        
        
                                                                                                                                                                                 
#======================================================

main()


