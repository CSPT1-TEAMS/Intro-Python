class Weapon
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "Fist-sized rock, great for bludgeoning."
        self.damage = 5

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "Small rusty dagger. Slightly more dangerous than a rock."
        self.damage = 10

class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This old sword has rusted with age, but it still has some fight in it."
        self.damage = 20

        