class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return 'Item name: ' + self.name + '\n' + 'Item Description: ' + self.description + '\n\n'
    def pickup_item(self, player):
        player.items.append(self)
        player.room.items.remove(self)

class Money(Item):
    def __init__(self, name, description, amnt):
        super().__init__(name, desciprion)
        self.amnt = amnt
    
