
"""
Written by Albert "Anferensis" Ong

Assigns default values in the game engines global dictionary.
"""

from bge import logic


def main():
    
    global_dict = logic.globalDict
    
    # Will only load defaults one time.
    if global_dict == {}
    
        logic.globalDict["Volume"] = 1.0
    


#======================================================

main()


