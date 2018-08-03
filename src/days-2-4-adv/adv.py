from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside the Home entrance", "North of you, the doors beckon"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("#     Treasure Chamber     #", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),    
    'library': Room("#     library     #", """You have found a place for reading. Unfortunately In your adventures you never learned the Dewey Decimal System so finding books is very difficult"""),

    'breakfastnook': Room("#     Breakfast nook     #", """Just off the kitchen a breakfast nook ending in a large curved window setting overlooking a large yard. Looks pretty nice. I wonder what Wait why am I here?"""),
    'livingroom': Room("#     Living Room     #","""You find a lavish 30 by 20 foot living room. an ornate table sits in front of the fireplace flanked by two sofas. The fire still crackling. The room looks dustless and well kept"""),

    'kitchen': Room("#     Kitchen      #", """In front of you, a modern kitchen. outfitted with all the trappings a home of this size should have with one exception you notice. "where is the fridge?"""),

    'staircase': Room("#      staircase      #", """You walk up the an iron railing staircase to you right assorted pictures of a family. You dont recognize any of them. but they look happy """),

    'secretroom': Room("#      ~An unplaned room has no name~      #", """ you find a secret room of someones design. outfitted with a small collection of books and a desk you wonder if anything here is worth keeping a secret? you see a dimmly lit staircase going down"""),

    'sprialstaircase': Room("#      ~Sprial Staircase~      #", """ a large sprial staircase decends into darkness lit only by the light of a single torch on the wall """),

    'landing': Room("#      Staircase landing      #", """ The staircase ends on a landing to the west a large room. to the east you see streaks of light from a window at the end. rooms on both sides of the hallway  """),

    'longhallway1': Room("#      Hallway      #", """ The staircase ends on a landing to the west a large room. to the east you see streaks of light from a window at the end. rooms on both sides of the hallway  """),
    
    'longhallway2': Room("#      Hallway      #", """ The staircase ends on a landing to the west a large room. to the east you see streaks of light from a window at the end. rooms on both sides of the hallway  """),
    
    'bedroom1': Room("#      Bedroom      #", """ Its a bedroom what do you expect...... you find piece of paper missing 3 letters  a---  """),
    
    'bedroom2': Room("#      Bedroom      #", """ Its a bedroom what do you expect -b--  """),
    'bedroom3': Room("#      Bedroom      #", """ Its a bedroom what do you expect --c- """),
    'bedroom4': Room("#      Bedroom      #", """ Its a bedroom what do you expect  ---d """),
    'bedroom5': Room("#      Master Bedroom      #", """ Its a bedroom what do you ex.... you find a mirror. You see yourself for seemingly the first time. a shiver runs down your spine """),
    
    'largecolumedexpanse': Room("#      ~Large columned expanse~      #", """ columns 4 feet wide are space evenly across the this large 50 foot tall 40 ft wide expanase. darkness is before you. westward into the darkness or east to cowardice """),
    'largecolumedexpanse2': Room("#      ~Large columned expanse~      #", """ you see as you press forward a large fire pit within a wide opening copper pot. the smell of gasoline is strong. its pretty dark in here might be easier to see with light you think. westward further into the hall or east toward cowardice """),
    'largecolumedexpanse3': Room("#      ~Large columned expanse~      #", """ you find a wall. empty of defects like the other room. A dead end....  East toward cowardice??? """),
    'balcony': Room(" Balcony ", """you find a door to a balcony, stepping out fresh air greets you.  west to go back inside""")

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
room['largecolumedexpanse'].s_to = room['sprialstaircase']

# room['Litlargecolumedexpanse'].e_to = room['Litlargecolumedexpanse2']
# room['Litlargecolumedexpanse2'].e_to = room['Largecolumedexpanse3']
# room['Litlargecolumedexpanse2'].w_to = room['Largecolumedexpanse']
# room['Litlargecolumedexpanse3'].w_to = room['Largecolumedexpanse2']
# room['Litlargecolumedexpanse'].s_to = room['sprialstaircase']


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
    elif bob.room.w_to == None:
            print(' #BAM!~~~ A wall finds purchase on your forehead. Try another path')
        # elif Player.room.w_to == False:
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
print("Game exited ..... or did the game exit you?")
# If the user enters "q", quit the game.
