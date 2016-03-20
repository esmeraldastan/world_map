import sys

node = None 

class building:
    
    def __init__(self, name, description, up, down, north, east, south, west, right, left, outside, inside ):
        self.name = name
        self.description = description
        self.up = up
        self.down = down
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.right = right
        self.left = left
        self.outside = outside 
        self.inside = inside 
        
        def move(self, direction):
            global node 
            node = globals()[getattr(self, direction)]
            
#BUILDING
#THIRD FLOOR            
main_office = building('Office', 'Papers have been shattered.', None, None, 'Conference Room', 'Secutary Desk', None, None, None, None, None, None)
elevator = building('Elevator', '', None, None, None, None, 'Secutary Desk',None, None, None, None, None)
meeting_room = building('Conference Room', '', None, None, None, 'Elevator', 'Secutary Desk',None, None, None, None, None)
stairs  = building ('Stairs', '', None, None, None, None, None,None, None, None, None, None)
secutary_office = building('Secutary Desk', '', None, None, None, None, None , None, None, None, None, None)

#SECOND FLOOR
weapon_room = building('', '', None, None, None, None, None,None, None, None, None, None)
secret_door = building('', '', None, None, None, None, None,None, None, None, None, None)
ganiter_room = building('', '', None, None, None, None, None,None, None, None, None, None)
bathroom = building('', '', None, None, None, None, None,None, None, None, None, None)
room1 = building ('', '', None, None, None, None, None,None, None, None, None, None)
room2 = building ('', '', None, None, None, None, None,None, None, None, None, None)

#FIRST FLOOR


#OUTSIDE 
insurence_building=('', '', None, None, None, None, None,None, None, None, None, None)
coffee_shop = ('', '', None, None, None, None, None,None, None, None, None, None)
bank =('', '', None, None, None, None, None,None, None, None, None, None)

node = main_office 

#Run program 

while True:
    print node
    print "Room: " + node.name
    print 
    print "Description: " + node.description 
    
    response = ['up', 'down', 'north', 'east', 'south', 'west', 'right', 'left', 'outside', 'inside'] 
    
    command = raw_input('>').strip().lower()
    #QUITE THE PROGRAM 
    if command in ['q', 'exit', 'quit']:
        sys.exit(0)
    #MOVE INTO DIFFERNT ROOMS 
    if command in response:
        try:
           node.move(command)
        except:
           print 'You can\'t do that way! '   
        

