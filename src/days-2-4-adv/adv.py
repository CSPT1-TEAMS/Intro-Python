from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player( 'Greg', room['outside'] )

# print(greg.room)

# Write a loop that:
print( f"Welcome, {player.name}! Let's begin our adventure." )
print(player.room, "\n", player.room.description)
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
# print(greg.room, "\n", greg.room.description)

while not dir == "q":
    # * Waits for user input
    # print("\n")
    dir = input("Please enter a direction...n, s, e, w OR q to quit game. \n")
    if dir is "n" or dir is "s" or dir is "e" or dir is "w":
        if hasattr(player.room, dir + '_to'):
            player.room = getattr(player.room, dir + '_to')
            print("---------")
            print(player.room, "\n", player.room.description)
            print("---------")
        else:
            print("You have made an invalid entry. Try again.")
    elif dir != "q":
        print("Please choose direction or q to quit")
    #  decides what to do.
    # if north
    # elif south
    # elif east
    # elif west
    # elif quit
    # elif invalid choice

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.

    # If the user enters "q", quit the game.
print("You have quit")
"Exit"