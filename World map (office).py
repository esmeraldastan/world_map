import sys

node = None 

class building:
    
    def __init__(self, name, description, up, down, east, west, north, south, left, right):
        self.name = name
        self.description = description
        self.up = up
        self.down = down
        self.east = east
        self.west = west
        self.north = north
        self.south = south
        self.left = left
        self.right =right
        
        def move(self, direction):
            global node 
            node = globals()[getattr(self, direction)]
            
#BUILDING
#THIRD FLOOR            
main_office = building('Office', 'Papers have been shattered.', None, None, None, None, None,None, None, None)
elevator = building('', '', None, None, None, None, None,None, None, None)
room1 = building('', '', None, None, None, None, None,None, None, None)
stairs  = building ('', '', None, None, None, None, None,None, None, None)
meeting_room = building('', '', None, None, None, None, None,None, None, None)
secutary_office = building('', '', None, None, None, None, None,None, None, None)

#SECOND FLOOR
weapon_room = building('', '', None, None, None, None, None,None, None, None)
ganiter_room = building('', '', None, None, None, None, None,None, None, None)
bathroom = building('', '', None, None, None, None, None,None, None, None)
secret_door = building ('', '', None, None, None, None, None,None, None, None)

#FIRST FLOOR


node = main_office 

command = raw_input('>').strip().lower()
if command in ['q', 'exit', 'quit']:
    sys.exit(0)

