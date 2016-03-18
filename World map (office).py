import sys

#Name of the Game 
print "Welcome to CounterCode"



node = None 

class building:#starting of the game 
    
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
            
#Building
#first floor                        
main_office = building('Office', 'Papers have been shattered.', None, None,'Secutary Desk', "Meeting Room", None,None, None, None)
elevator = building('Elevator', '', None, None, None, None, None,None, None, None)
secutary_office = building('Secutary Desk', '', None, None, None, None, None,None, None, None)
stairs  = building ('Stairs', '', None, None, None, None, None,None, None, None)
meeting_room = building('Meeting Room', '', None, None, 'Elevator', None, None, 'Office', None, None)

#second floor
weaponary_room = building('Secret Room', '', None, None, None, None, None,None, None, None)
ganitor_room = building(' ', '', None, None, None, None, None,None, None, None)
office1 = building('', '', None, None, None, None, None,None, None, None)
office2 = building('', '', None, None, None, None, None,None, None, None)
office3= building ('', '', None, None, None, None, None,None, None, None)
bathroom = building ('', '', None, None, None, None, None,None, None, None)

#first floor

#city
bank = building ('Bank', '', None, None, None, None, None,None, None, None)
coffee_shop = building ('Coffee Shop', '', None, None, None, None, None,None, None, None)
building2 = building ('Insurence Building', '', None, None, None, None, None,None, None, None)
drug_store = building ('Pharmacy ', '', None, None, None, None, None,None, None, None)




node = main_office 

command = raw_input('>').strip().lower()
if command in ['q', 'exit', 'quit']:
    sys.exit(0)

