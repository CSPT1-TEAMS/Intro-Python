# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def print_items(self, player):
        if len(self.items) == 0:
            print("No items in the " + player.room.name)
        else:
            print('Items in this room:\n')
            for item in self.items:
                print('\t', item)

