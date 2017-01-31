
"""
Written by Albert "Anferensis" Ong

Controls the visual effects involved with moving
the stage cards.
"""

from bge import logic


def move_stage_cards(owner, direction):
    
    isLeft = direction == "Left"
    isRight = direction == "Right"
    
    if isLeft:
        
        add_stage_num = -1       
        add_x = 1.75
              
    elif isRight:
        
        add_stage_num = 1       
        add_x = -1.75
            
    owner.position.x += add_x   
    
    old_stage_num = owner["Stage Number"]
    owner["Stage Number"] += add_stage_num
    new_stage_num = owner["Stage Number"]
        
    objects = logic.getCurrentScene().objects    
       
    stage_cards_dict = {
    
        -2: "Stage Card -02",
        -1: "Stage Card -01",
         0: "Random Stage Card",
         1: "Stage Card 01",
         2: "Stage Card 02", }
         
    old_stage_card_name = stage_cards_dict[old_stage_num]
    new_stage_card_name = stage_cards_dict[new_stage_num]
    
    old_stage_card = objects[old_stage_card_name]
    new_stage_card = objects[new_stage_card_name]
    
    old_stage_card.color = [1.0, 1.0, 1.0, 0.25]
    new_stage_card.color = [1.0, 1.0, 1.0, 1.0]
    
    old_stage_card.scaling = [1.0, 1.0, 1.0]
    new_stage_card.scaling = [1.4, 1.4, 1.0]
    
    old_stage_card_border = old_stage_card.children[0]
    new_stage_card_border = new_stage_card.children[0]
    
    old_stage_card_border.color = [1.0, 1.0, 1.0, 0.25]
    new_stage_card_border.color = [1.0, 1.0, 1.0, 1.0]    
    
    
    stage_names_dict = {
    
        -2: "ROCK CONCERT",
        -1: "GAME TEST",
         0: "RANDOM",
         1: "BELAIR ESTATE",
         2: "SUNSET PIER", }  
    
    stage_select_text = objects["Stage Select Text"]
    stage_name = stage_names_dict[new_stage_num]
    stage_select_text.text = stage_name
       
           
    isMax = new_stage_num == 2
    isMin = new_stage_num == -2
    
    if isMin:               
        owner["Left End"] = True
           
    elif isMax:
        owner["Right End"] = True
        
    else:        
        owner["Left End"] = False
        owner["Right End"] = False
    
    
    subject = str(new_stage_num)    
    owner.sendMessage(subject, "", "Stage Card")
            
            
    
def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    left = owner.sensors["Left"]
    right = owner.sensors["Right"]


    if left.positive and not owner["Left End"]:
        
        move_stage_cards(owner, "Left")
        cont.activate("Move Sound")
        
    elif right.positive and not owner["Right End"]:
        
        move_stage_cards(owner, "Right")
        cont.activate("Move Sound")

        
        
#======================================================

main()


