import items

class Player:
    def __init__(self):
        self.inventory = [items.Rock(),
                          items.Dagger(),
                          'Gold(5)',
                          'Crusty Bread']

    def print_inventory(self):
        print("Inventory: ")
        for i in self.inventory:
            print("* " + str(i))
        best_weapon = self.most_powerful_weapon()
        print("Your best weapon is your {}".format)

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for i in self.inventory:
            try:
                if i.damage > max_damage:
                    best_weapon = i
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

        