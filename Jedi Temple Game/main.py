# Blake Kemp 
# jedi Temple Text Game 
#IT-140

#Define the game instructions.
def instructions(): 
    print('Welcome to the Jedi-Temple Adventure Game')
    print('The fate of the galaxy rests in your hands Padawan, collect all 6 items to defeat Darth Sidious.')
    print('To move from room to room: go north, go south, go east, go west')
    print('Add items to your inventory: get (item name)')
    print('Type quit to end the game') 



#Dictionary that links one room to another with their assigned item in the room.
rooms = {
    'Temple Great Hall': {'south': 'Temple Infirmary', 'north': 'Training Ground', 'east': 'Count Dooku\'s Quarters', 'west': 'Jedi Archives'},
    'Training Ground': {'south': 'Temple Great Hall', 'east': 'Yoda\'s Quarters', 'item': 'lightsaber'},
    'Yoda\'s Quarters': {'west': 'Training Ground', 'item': 'jedi book'},
    'Temple Armory': {'south': 'Count Dooku\'s Quarters', 'item': 'darth sidious'},
    'Count Dooku\'s Quarters': {'north': 'Temple Armory' , 'west': 'Temple Great Hall', 'item': 'wayfinder'},
    'Jedi Archives': {'east': 'Temple Great Hall', 'item': 'holocron'},
    'Temple Infirmary': {'north': 'Temple Great Hall', 'east': 'Jedi Council Chamber', 'item': 'healing crystal'},
    'Jedi Council Chamber': {'west': 'Temple Infirmary', 'item': 'jedi credit'}
}
#outlines starting room
def get_new_room(room, direction):
    '''Function for moving through the rooms'''
    new_room = room #declaring
    for i in rooms: #Loop
       if i == room: 
            if direction in rooms[room]: 
                new_room = rooms[room][direction] #assigning new_ room
    return new_room

#Describes the ITEM and what it does for the user.
item_descr = {
        'get lightsaber': 'You grab the lightsaber and hold it over your head knowing that you will avenge your master.',
        'get jedi book': 'The book gives you the knowledge on how to defeat a Sith Lord.',
        'get wayfinder': 'The wayfinder tells you the whereabouts of the Sith within the Temple.',
        'get holocron': 'The holocron gives you the wisdom of Master Yoda.',
        'get healing crystal': 'Using the crystal you regain all your energy and fully heal any ailment.',
        'get jedi credit': 'Only given to true Jedi Masters, for only a Master can truly defeat the Sith Lord.',
    }

    #Game play loop
def main():
    print()
    instructions()
    inventory = list()
    room = 'Temple Great Hall'
    while (1): #Gameplay Loop
        print('************************************************************')
        print()
        print ('You are in', room) # Tells you what room you're in
        print('Inventory:', inventory) #Tells you whats currently in your inventory
        if 'item' in rooms[room]:
            print('You see a ' + rooms[room]['item']) #If an item is in the room, outputs which item it is.
        direction = input ('Enter your move: ') #User input
        if direction == 'quit':
            exit(0) #if 'quit' then the game exits
        if (direction == 'go east' or direction == 'go west' or direction == 'go north' or direction == 'go south'): #Cardinal directions
            direction=direction[3:]
            new_room = get_new_room(room, direction) # calLing function for valid room
            if new_room == room: # if no room in that direction, outputs for another direction
                print ('The room has wall in that direction enter other direction!')
            elif new_room == 'Temple Armory': #if user goes to the Temple Armory then the user LOSES. 
                print ('You were slayed by the Sith Lord!!, You Lose.')
                exit(0) #End of Game 
            else:   
                room = new_room 
        elif direction == str('get ' + rooms[room]['item']): #if user input is to get item
            if rooms[room]['item'] in inventory: #if item already present in inventory
                print ('Item already taken go to another room!!')
            else:
                print('You picked up ' + rooms[room]['item'])
                print()
                print(item_descr.get('get ' + rooms[room]['item'])) #Grabs the Item from item_descr and tells user what it does.
                inventory.append(rooms[room]['item']) #If item picked up, append to the inventory list.   
        else:
            print ('Invalid direction!!') # If wrong command 
        if len(inventory)==6:
            print ('Congratulations! You have collected all items and slayed the Sith Lord!,\nMAY THE FORCE BE WITH YOU!!') #Once all 6 items have been collected, user WINS the game. 
            exit(0)
if __name__=='__main__':
    main()
