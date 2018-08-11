class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
         
    def __str__(self):
        return self.name

    def on_grab(self, player):
        print("grabbing")
        if self.picked_up == False:
            # update treasure
            # player.score += self.value
            self.picked_up == True
    
    def on_drop(self, player):
        Link.room.items.append(self)
        # remove item from possession
        Link.items.remove(self)

class Key( Item ):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.picked_up = False

    def __str__(self):
        return self.name

    def on_grab(self, player):
        super().on_grab(player)
        if self.picked_up == False:
            self.picked_up == True

    def on_drop(self, player):
        player.room.items.append()
        # remove item from possession
        player.items.remove()

class Treasure( Item ):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.name = name
        self.picked_up = False

    def on_grab(self, player):
        super().on_grab( player)
        if self.picked_up == False:
            # update treasure
            player.score += self.value
            self.picked_up == True



# class Hp(Item):
#     def __init__(self, name, description, value):
#         super().__init__(name, description)
#         self.hp = hp
#         self.picked_up = False

#     def on_grab(self, player):
#         super().on_grab(player)
#         if self.picked_up == False:
#             # update treasure
#             player.life += self.value
#             self.picked_up == True


class Master_Sword( Item ):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        self.picked_up = False

    def __str__(self):
        return self.name
    
    def on_grab( self, player ):
        super().grab(self, player)

