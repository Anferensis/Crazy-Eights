
"""
Written by Albert "Anferensis" Ong

Controls victory screen properties based on the winner.
"""

import aud
import os
from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    # Changes the directory towards where the victory themes are stored.
    os.chdir(logic.expandPath("//"))
    os.chdir("../../Sound Files/UI SFX/")
    
    try:
        winner = logic.globalDict["Winner"]
        
    except KeyError:
        winner = "Marth"
    
    device = aud.device()
    delay = cont.sensors["Delay"]
    
    if not delay.positive:

        theme_path = "Victory Themes/" + winner + "_victory_theme.ogg"
        victory_theme = aud.Factory.file(theme_path)
        device.play(victory_theme)
        
        quote_path = "Victory Quotes/" + winner + "_victory_quote.ogg"
        quote = aud.Factory.file(quote_path)
        device.play(quote)
        
        cont.activate("This game's winner is")
    
    
    else:
        
        announcer_path = "Melee Announcer/Character/" + winner + ".ogg"
        character_name = aud.Factory.file(announcer_path)
        
        device.play(character_name)



#======================================================

main()


