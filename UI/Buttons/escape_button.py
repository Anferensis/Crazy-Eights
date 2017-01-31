
"""
Written by Albert "Anferensis" Ong

Activated when pressing the escape button.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    escape = owner.sensors["Escape"]
    
    if escape.positive:
        
        bgm = owner.actuators["BGM"]
        bgm.volume *= 0.2
        
        for act in ("Pause Menu", "Suspend Main", "Suspend Overlay"):
            cont.activate(act)
    
    

#======================================================

main()


