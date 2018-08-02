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
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['overlook'].w_to = room['library']
room['library'].e_to = room['overlook']

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
