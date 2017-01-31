
"""
Written by Albert "Anferensis" Ong

Controls all attack and movement inputs for a character.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    
    sensor_inputs = []
    
    for sensor_name in ("Up Tap", "Up Hold", "Down", "Left", "Right", 
                        "Primary", "Secondary", "Shield", "Taunt",  
                        "Strong", "isGround"):
                            
        sensor = cont.sensors[sensor_name]
        is_positive = int(sensor.positive)               
        sensor_inputs.append(is_positive)
        
        var_name = sensor_name.lower()
        var_name = var_name.replace(" ", "_")
        globals()[var_name] = sensor
        
  
        
    viable_inputs = owner["viable_inputs"]
  
    # Searches for a viable attack input.
    try:                 
        action_name = viable_inputs[tuple(sensor_inputs)]

        armature = owner.children[0].name
        shield = owner.children[1].name
        
        
        if action_name in ("Idle", "Taunt", "Shield", "Neutral", "Up Neutral", 
                           "Down Neutral", "Forward Neutral", 
                           "Up Jazz", "Down Jazz", "Forward Jazz", 
                           "Neutral Aerial", "Up Aerial", "Down Aerial", "Forward Aerial", "Back Aerial",): 
                                                             
            owner.sendMessage(action_name, "", armature)
            
            if action_name == "Taunt":            
                cont.activate("Taunt Sound")
        
            
        if action_name in ("Shield", "Spot Dodge", "Roll", "Air Dodge"):
            owner.sendMessage(action_name, "", shield)
        
                      
    
    # Otherwise searches for a movement input.        
    except KeyError:
        
        
        jumps = owner["Jumps"]
        
        if up_tap.positive and jumps < 2:
            cont.activate("Jump")
            cont.activate("Jump Sound")
            owner["Jumps"] += 1
        
           
        elif down.positive:
            
            if isground.positive:
                armature_name = owner.children[0].name
                #owner.sendMessage("Crouch", "", armature_name)
            
            else:
                cont.activate("Down")
        
               
        if left.positive:
            
            if isground.positive:
                cont.activate("Left")
            else:
                cont.activate("Left Air")
        
               
        elif right.positive:
            
            if isground.positive:
                cont.activate("Right")
            else:
                cont.activate("Right Air")
   
   
    # Deactivates all movement inputs at the end of the script.
    # This is necessary, otherwise movement actuators will run indefinitely.
    for act_name in ("Jump", "Down", "Left", "Right", "Left Air", "Right Air"):
   
        cont.deactivate(act_name)
    


#======================================================

main()


