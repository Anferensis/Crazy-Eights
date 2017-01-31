
"""
Written by Albert "Anferensis" Ong

Activated when pressing the resume button.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    click = owner.sensors["Click"]
    mouse_over = owner.sensors["Mouse Over"]
    unpause = owner.sensors["Unpause"]
    
    if (click.positive and mouse_over.positive) or unpause.positive:
        
        main_scene = logic.getSceneList()[0]
        stage_props = main_scene.objects["Stage Properties"]
        bgm = stage_props.actuators["BGM"]
        bgm.volume /= 0.2
        
        for act in ("Remove Pause", "Resume Main", "Resume Overlay", \
					 "Remove Mouse"):
            
            cont.activate(act)
            
    
            
#======================================================

main()


