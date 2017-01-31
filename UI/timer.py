
"""
Written by Albert"Anferensis"Ong

Properly formats the minutes timer in the game.
"""

from bge import logic

def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    objects = logic.getCurrentScene().objects
    props = objects["Overlay Properties"]
    
    total_time = props["Total Time"]
    current_time = props["Timer"]
    time_difference = int(total_time - current_time)
    
    minutes = str(time_difference // 60)
    seconds = str(time_difference % 60)
    
    seconds = seconds if len(seconds) == 2 \
         else "0" + seconds
    
    owner["Text"] = ":".join([minutes, seconds])



#==================================================

main()


