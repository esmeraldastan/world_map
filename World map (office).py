# -*- coding: utf-8 -*-
import time 
import sys

#Name of the Game 
time.sleep(0.5)
print "Welcome to CounterCode\n"

print "Your obective in this game will be to get out of\nthe building to safety.\n"  


node = None 

class Building:#start of the map 

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
        
#INTO TO THE GAME        
print 'You have woken up from a long sleep. The last thing you remember was escaping\nthe white gas that was spreading throughout the city.' 
           
#BUILDING

#THIRD FLOOR            
Office = Building("Office", 'Papers have been shattered everywhere. The lights a\nflashing on and off. There next to you is a light blue paper. Type "pick up" to read what it says.', None, None, 'Conference', 'Secutary', None, None, None, None, None, None)
Conference = Building("Conference Room", 'You are now standing in the Conference Room. A couple of bodies are laying around. Rottening with a nasty smell. There\'s a flashlight on the table. Pick it up...you might need it later on .', None, None, None, 'Elevator', 'Office',None, None, None, None, None)
Elevator = Building("Elevator", 'In the Elevator head down to continue getting to your destination. Type "down".But wait before that you you need to restore to full health.There is a green cyrum laying on the grown. Type "restore" this will get you to full health. ', None, 'Elevator2', None, None, 'Secutary Desk',None, None, None, None, None)
Stairs = Building("Stairs", 'The walls are coverd with blood. You are not alone. Zombies and infecteds run the area now. You don\'t want to encounter with one ...it can be your end.To go down the stairs type down to go on to the next floor.There is blood covering the walls….Bodies laying down with body parts missing. Be careful.  ', None, 'Stairs1', None, None, None,None, None, None, None, None)
Secutary = Building("Secutary Desk",' You are standing next to your securary\'s desk. A flash light stands on top. Pick it up you might need it later on. Head "north" to the elevator or "east" to the stairs.', None, None, 'Elevator', None, None , None, None, None, None, None)

#PATH TO SECOND FLOOR
Stairs1 = Building("Stairs", '', None, None, None, None, None,None, None, None, None, None)
#SECOND FLOOR
Weapon = Building('Weapon Room', '', None, None, None, None, 'Secret',None, None, None, None, None)
Secret = Building('Secret Door', '', None, None, 'Weapon', 'Janitor', None,None, None, None, None, None)
Janitor= Building('Janitor Room', '', None, None, None, 'Office1', 'Secret',None, None, None, None, None)
Bathroom = Building('Restroom', '', None, None, None, None, 'Stairs','Elevator', None, None, None, None)
Office1 = Building('Office 1', '', None, None, 'Elevator', 'Office2', 'Janitor',None, None, None, None, None)
Office2 = Building('Office 2 ', '', None, None, None, 'Elevator', 'Stairs','Office1', None, None, None, None)

Stairs2 = Building("Stairs", 'You are now in the first floor. Zombies are following you down. Place the bomb in between the stairs and the front desk. Type "place". Once you do head out.', None, None, None, None, None,None, None, None, None, None)
#FIRST FLOOR
Front = Building('', '', None, None, None, None, None,None, None, None, None, None) 
Door = Building('', '', None, None, None, None, None,None, None, None, None, None)
Building('', '', None, None, None, None, None,None, None, None, None, None)
#OUTSIDE 
insurence_building=('', '', None, None, None, None, None,None, None, None, None, None)
coffee_shop = ('', '', None, None, None, None, None,None, None, None, None, None)
bank =('', '', None, None, None, None, None,None, None, None, None, None)

node = Office

#Run program 

while True:
    print node
    print "Room: " + node.name
    print 
    print "Description: " + node.description 
    
    #WORD DEFINE
    infected = "A person who had been contaminated by the gas"
    zombie = 'A dead person risen from the dead.The chemicals within the gass had an effect on the dead makeing them come back to life'
    
    response = ['up', 'down', 'north', 'east', 'south', 'west', 'right', 'left', 'outside', 'inside'] 
    pick = ['pick up']
    command = raw_input('>').strip().lower()
    #QUITE THE PROGRAM 
    if command in ['q', 'exit', 'quit']:
        sys.exit(0)
    #paper read out 
    if command in pick:
        print 'Escape to th labatory hidden under the old facotry building.It should be located a couple of blocks\nwest of where you are located.'
        print 'Head north or east'
    #MOVE INTO DIFFERNT ROOMS 
    if command in response:
        try:
           node.move(command)
        except:
           print 'You can\'t do that way! '   
        


