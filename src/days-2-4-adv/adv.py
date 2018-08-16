from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'library': Room('Library',
                    'The universe (which others call the Library) is composed of an indefinite, perhaps infinite number of hexagonal galleries.',
                    Item('Book', 'It looks like the heaviest book you\'ve ever seen')),
                    
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     Item('Book', 'It looks like the heaviest book you\'ve ever seen')),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty
                     passages run north and east.""",
                     Item('Book', 'It looks like the heaviest book you\'ve ever seen')),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling
                     into the darkness. Ahead to the north, a light flickers in
                     the distance, but there is no way across the chasm.""",
                     Item('Book', 'It looks like the heaviest book you\'ve ever seen')),

    'narrow':   Room("Narrow Passage",
                     """The narrow passage bends here from west
                     to north. The smell of gold permeates the air.""",
                     Item('Book', 'It looks like the heaviest book you\'ve ever seen')),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure
                     chamber! Sadly, it has already been completely emptied by
                     earlier adventurers. The only exit is to the south.""",
                     Item("Treasure Chest", "You've hit the motherload.")),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['library']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['library'].e_to = room['foyer']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
andrew = Player('Andrew', room['outside'], [Item(
    'Old Notebook',
    """You seem to be holding an old, water-stained notebook.
    Some of the pages appear to be torn out, although you can almost make out
    what was scribbled onto the last page... it looks like it might be someone's name.""")]
)

cmd = ''
done = False

def print_room_info():
    print(andrew.room.name)
    print(andrew.room.description)
    andrew.room.print_items(andrew)

while not done:
    print_room_info()

    cmd = input(
        """Please enter a command:
        \n
        \t - choose a direction (n,s,e,w),
        \t - grab an item (g <name_of_item>)
        \t - quit (q)
        \t - view inventory (i)
        \n
        """)

    if cmd == 'q':
        done = True

    # elif cmd in ['n','s','e','w']:
    #     if cmd == 'n':
    #     if cmd == 's':
    #     if cmd == 'e':
    #     if cmd == 'w':



# Write a loop that:
#
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
