
"""
Written by Albert "Anferensis" Ong

Controls percent text shaking.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    hit = owner.sensors["Hit"]
    
    
    if hit.positive:
        
        damage = int(hit.subjects[0])
                       
        owner["Percent"] += damage
        percent_str = str(owner["Percent"])
        
        spacing_dict = { 1 : "    ",
                         2 : "  ",
                         3 : "" }
        
        percent_len = len(percent_str)                 
        spacing = spacing_dict[percent_len]
        
        new_percent_text = spacing + percent_str
        owner.text = new_percent_text  
        
               
        if  damage < 15:            
            cont.activate("Shake")
                    
        elif damage >= 15:            
            cont.activate("Shake Strong")
    
        

#======================================================

main()


