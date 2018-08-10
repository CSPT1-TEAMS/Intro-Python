from player import Player
from room import Room
from item import Item

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons""", []),
 
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("key", "Key unlocks a treasure")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """Navy: HEY, LISTEN! This treasure requires a key. 
We should be able to find it in this dungeon! You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("sword","sharp")]),
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
Link = Player(room['outside'], [])
cmd = ""
# Write a loop that:
def print_room_info():
# * Prints the current room name
    print("\nHey Listen! We are in room", Link.room.name)
# * Prints the current description (the textwrap module might be useful here).
    print(Link.room.description)
    print(Link.items)
# * Waits foLinkr user input and decides what to do.
    # print( Link.room.view_items())
    print("\nItems found in this room: ")
    if len(Link.room.items) == 0:
        print("      none")
    else:
        for i in Link.room.items:
            print("\n .: " + i.name)

def has_key():
    for i in Link.items:
        if i.name == "key":
            return True
    return False

def has_sword():
    for i in Link.items:
        if i == "sword":
            return True
        return False


# cmd = print_help()
cmd_menu = "\n < ---.: ^ : .--------Welcome to Hyrule--------.: ^ : .---> \n \nPlease enter a direction... w, s, a, d to move \n \nk to pick up/use an item and j to use the sword. \nq to quit the game\n \n"

while not cmd == "q":
    cmd = input(cmd_menu)
# If the user enters a cardinal direction, attempt to move to the room there.
    if Link.hp == 0:
        print("You lose!")
        # cmd = "q"
        exit()
        
    if Link.room.items:
        print(Link.room.has_items())

    parsed_cmd = cmd.split()
    if len(parsed_cmd) > 1:
        print(parsed_cmd)
        action = parsed_cmd[0]
        item = ""
        for i in range(1, len(parsed_cmd)):
            item += parsed_cmd[i] + " "
        item = item.strip() # to remove extra trailing space 
        
        if action == "g" or action == "grab":
            for i in Link.room.items:
                print(i)
            for i in Link.room.items:
                if parsed_cmd[1] == i.name:
                    i.on_grab(Link)
                    Link.grab(i)

            cmd = input()

    elif cmd == "hp":
        cmd = input("Life: " + str(Link.hp) + "\n")

    elif cmd == "u" or cmd == "use":
        for i in Link.items:
            if parsed_cmd[1] == i.name:
                print(i)
            for i in Link.items:
                if parsed_cmd[1] ==i.name:
                    i.on_drop(Link)
                    Link.drop(i)
            cmd = input()
            
    #elif action == "o" or action =="open"

    elif cmd == "j":
        if has_sword():
            print("~slash~")
        else:
            print("Navy: LISTEN! We need to find you a weapon")
    elif cmd == "n":
        print(print_room_info())
#if north
    elif cmd == "w":
        if hasattr(Link.room, "n_to"):
            Link.room = Link.room.n_to
        else:
            print("Navy: LISTEN! Seems like you can't move in that direction")
    # elif south
    elif cmd == "s":
        if hasattr(Link.room, "s_to"):
            Link.room = Link.room.s_to
        else:
            print("Navy: HEY! Where are you going?!")
    # elif east
    elif cmd == "a":
        if hasattr(Link.room, "e_to"):
            Link.room = Link.room.e_to
        else:
            print("Can't go there")
    # elif west
    elif cmd == "d":
        if hasattr(Link.room, "w_to"):
            Link.room = Link.room.w_to
        else:
            print("Navy: Where are you going? Nothing that way!")
    # elif quit
    elif cmd == "q":
        print("Navy: Thanks for playing!")
    # else invalid
    else:
        cmd = input("\nInvalid selection.\n")
# use has_attribute to see if the user can move in that direction


# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
