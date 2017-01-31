
"""
Written by Albert "Anferensis" Ong
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    owner["frame_data"] = {
    
        "Neutral Aerial" :
        
            { "phases" : ("phase1", "phase2"), 
            
            
              "phase1" : { 
             
                 "active_frames" : range(4, 9), 
                 "hitboxes" : ("07", "08", "09", "10"), 
                 
                 "hitbox_data_07" : {
                    "color" : "red", 
                    "damage" :  10, 
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.50 }, 
                    
                 "hitbox_data_08" : {
                     "color" : "red",
                     "damage" :  10, 
                     "hitstun" : 0, 
                     "force_x" : 0.08, 
                     "force_z" : 0.15, 
                     "scaling" : 0.50 }, 
                    
                 "hitbox_data_09" : {
                     "color" : "red",
                     "damage" :  10, 
                     "hitstun" : 0, 
                     "force_x" : 0.08, 
                     "force_z" : 0.15, 
                     "scaling" : 0.50 }, 
                    
                "hitbox_data_10" : {
                    "color" : "red",
                    "damage" :  10, 
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.50 },                 
                
                 },              
             
                 
             "phase2" : {
                           
                 "active_frames" : range(9, 32), 
                 "hitboxes" : ("07", "08", "09", "10"), 
                 
                                  
                 "hitbox_data_07" : {
                    "color" : "red", 
                    "damage" :  8, 
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.25 }, 
                    
                 "hitbox_data_08" : {
                     "color" : "red",
                     "damage" :  8, 
                     "hitstun" : 0, 
                     "force_x" : 0.08, 
                     "force_z" : 0.15, 
                     "scaling" : 0.25 }, 
                    
                 "hitbox_data_09" : {
                     "color" : "red",
                     "damage" :  8, 
                     "hitstun" : 0, 
                     "force_x" : 0.08, 
                     "force_z" : 0.15, 
                     "scaling" : 0.25 }, 
                    
                "hitbox_data_10" : {
                    "color" : "red",
                    "damage" :  8, 
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.25 }, 
                
                 },                                   
            },  
        
        
        
        "Forward Neutral" :
        
            { "phases" : ("phase1", ), 
            
            
              "phase1" : { 
             
                 "active_frames" : range(4, 9), 
                 "hitboxes" : ("09", "10"), 
                 
                    
                 "hitbox_data_09" : {
                     "color" : "red",
                     "damage" :  8, 
                     "hitstun" : 0, 
                     "force_x" : 0.05, 
                     "force_z" : 0.12, 
                     "scaling" : 0.25 }, 
                    
                "hitbox_data_10" : {
                    "color" : "red",
                    "damage" :  10, 
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.15, 
                    "scaling" : 0.35 },                 
                
                 },                   
            },
        }



#======================================================

main()


