
"""
Written by Albert"Anferensis"Ong

Runs the game over scenario.
Activated when a character runs out of stocks.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    game_over = owner.sensors["Game Over"]
    if game_over.positive:
        
        # Suspends the overlay.
        overlay = logic.getSceneList()[1]
        overlay.suspend()
        
        # Sets the game over text visible.
        gameover_text = overlay.objects["GAME!"]
        gameover_text.visible = True
        
        # Activates game over sound.
        cont.activate("Game Over Sound")
        
        
        # Exits the game after a delay.
        gameover_delay = owner.sensors["Game Over Delay"]
        
        if gameover_delay.positive == True:
            cont.activate("Exit Game")
    
    

#================================================

main()


