# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room, items):
        self.room = room
        self.items =  [ "shield", ]
        self.hp = ["hp", "hp", "hp", ]

    def __str__(self):
        return self.name

    def player_info(self, hp, items):
        print(self.hp)
        print(str(self.items))

    def grab(self, item):
        # item.on_grab()
        print("...Got", item)
        self.items.append(item)
        # remove item from room
        self.room.items.remove(item)
        # if self.picked_up == False:
        #     # update treasure
        #     player.items += self.value

    def drop(self, item):
        print("...Dropping!")
        self.items.remove(item)
        # remove item from room
        self.room.items.append(item)

