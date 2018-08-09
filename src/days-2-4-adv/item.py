class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return self.name + " " + self.description

    def on_grab():
        print("...Got it!")
        player.items.append(self)
        # remove item from room
        player.room.items.remove(self)
        if self.picked_up == False:
        # update treasure
            player.items += self.items


# class Treasure( Item ):
#     def __init__(self, name, description, value):
#         super().__init__(name, description)
#         self.name = name
#         self.picked_up = False

#     def on_grab(self, player):
#         super().on_grab( player )
#         if self.picked_up == False:
#             # update treasure
#             player.score += self.value
#             self.picked_up == True



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


# class Master_Sword( Item ):
#     def __init__(self, name, description, value):
#         super().__init__(name, description)
#         self.value = value
#         self.picked_up = False
    
#     def on_grab( self, player ):

