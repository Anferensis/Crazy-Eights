
"""
Written by Albert "Anferensis" Ong

Recieves a message from the parent object and activates
the animation listed in the message.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    message = cont.sensors["Message"]
    
    if message.positive:
        
        action_name = message.subjects[0]
        cont.activate(action_name)
        
        parent = owner.parent
        parent["Crouch"] = action_name == "Crouch"
        
        

#======================================================

main()


