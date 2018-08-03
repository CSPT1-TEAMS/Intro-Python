from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer [n] [s] [e] ", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
    'library': Room("library", """You have found a place for reading. Unfortunately In your adventures you never learned the Dewey Decimal System so finding books is very difficult""")

'library': Room("library", """You have found a place for reading. Unfortunately In your adventures you never learned the Dewey Decimal System so finding books is very difficult""")
    

}


# Link rooms together
room['outside'].n_to = room['foyer']

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['staircase']
room['foyer'].w_to = room['livingroom']
room['livingroom'].n_to = room['kitchen']
room['kitchen'].e_to = room['breakfastnook']
room['breakfastnook'].w_to = room['kitchen']

room['staircase'].n_to = room['landing']
room['foyer'].e_to = room['library']
room['staircase'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#upstairs
room['landing'].e_to = room['bedroom5']

room['landing'].w_to = room['longhallway1']
room['longhallway1'].w_to = room['longhallway2']
room['longhallway1'].s_to = room['bedroom2']
room['longhallway1'].n_to = room['bedroom1']
room['longhallway2'].w_to = room['balcony']
room['longhallway2'].n_to = room['bedroom3']
room['longhallway2'].s_to = room['bedroom4']

# room['overlook'].w_to = room['library']
room['library'].key_to = room['secretroom']
room['secretroom'].s_to = room['sprialstaircase']
room['secretroom'].n_to = room['library']
room['sprialstaircase'].n_to = room['secretroom']
room['sprialstaircase'].s_to = room['largecolumedexpanse']

room['largecolumedexpanse'].e_to = room['largecolumedexpanse2']
room['largecolumedexpanse2'].e_to = room['largecolumedexpanse3']
room['largecolumedexpanse2'].w_to = room['largecolumedexpanse']
room['largecolumedexpanse3'].w_to = room['largecolumedexpanse2']
room['Largecolumedexpanse'].s_to = room['sprialstaircase']

room['Litlargecolumedexpanse'].e_to = room['Litlargecolumedexpanse2']
room['Litlargecolumedexpanse2'].e_to = room['Largecolumedexpanse3']
room['Litlargecolumedexpanse2'].w_to = room['Largecolumedexpanse']
room['Litlargecolumedexpanse3'].w_to = room['Largecolumedexpanse2']
room['Litlargecolumedexpanse'].s_to = room['sprialstaircase']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
bob = Player(
    name = 'bob',
    room = room['outside']

)


# Write a loop that:
#

while not dir == "q":
    print(bob.room.name)
    print(bob.room.description)
# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).
    dir = input('Please enter a direction...n, s, e, w OR Q to quit the game')
# * Waits for user input and decides what to do.
    if dir == "n":
        if bob.room.n_to != None: 
            bob.room = bob.room.n_to
            # print(bob.room)
            # print(bob.room.description)
        # elif Player.room.n_to == False:
    elif dir == "s":
        if bob.room.s_to != None :
            bob.room = bob.room.s_to
        # elif Player.room.s_to == False:
    elif dir == "e":
        if bob.room.e_to != None:
            bob.room = bob.room.e_to
        # elif Player.room.e_to == False:
    elif dir == "w":
        if bob.room.w_to != None:
            bob.room = bob.room.w_to
        if bob.room.w_to == None:
            print(' #BAM!~~~ A wall finds purchase on your forehead. Try another path')
        # elif Player.room.w_to == False:
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
