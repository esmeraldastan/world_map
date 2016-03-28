import sys
node = None 

class Building:
    
    def __init__(self, name, description, up, down, north, east, south, west, right, left, outside, inside):
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
print 'You have woken up form a long sleep. The last thing you remember was escaping the white gass that was spreading throughout the city'            
#BUILDING
#THIRD FLOOR            
Office = Building("Office", 'Papers have been shattered.', None, None, 'Conference', 'Secutary', None, None, None, None, None, None)
Conference = Building("Conference Room", 'tables are shattered every where ', None, None, None, 'Elevator', 'Office',None, None, None, None, None)
Elevator = Building("Elevator", '', None, 'Elevator2', None, None, 'Secutary Desk',None, None, None, None, None)
Stairs = Building("Stairs", '', None, 'Stairs1', None, None, None,None, None, None, None, None)
Secutary = Building("Secutary Desk", '', None, None, 'Elevator', None, None , None, None, None, None, None)

Stairs1 = Building("Stairs", '', None, None, None, None, None,None, None, None, None, None)
#SECOND FLOOR
Weapon = Building('Weapon Room', '', None, None, None, None, 'Secret',None, None, None, None, None)
Secret = Building('Secret Door', '', None, None, 'Weapon', 'Janitor', None,None, None, None, None, None)
Janitor= Building('Janitor Room', '', None, None, None, 'Office1', 'Secret',None, None, None, None, None)
Bathroom = Building('Restroom', '', None, None, None, None, 'Stairs','Elevator', None, None, None, None)
Office1 = Building('Office 1', '', None, None, 'Elevator', 'Office2', 'Janitor',None, None, None, None, None)
Office2 = Building('Office 2 ', '', None, None, None, 'Elevator', 'Stairs','Office1', None, None, None, None)

#FIRST FLOOR
Front = Building('', '', None, None, None, None, None,None, None, None, None, None) 
Door = Building('', '', None, None, None, None, None,None, None, None, None, None)
Building('', '', None, None, None, None, None,None, None, None, None, None)
#OUTSIDE 
insurence_building=('', '', None, None, None, None, None,None, None, None, None, None)
coffee_shop = ('', '', None, None, None, None, None,None, None, None, None, None)
bank =('', '', None, None, None, None, None,None, None, None, None, None

node = Office

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
        

