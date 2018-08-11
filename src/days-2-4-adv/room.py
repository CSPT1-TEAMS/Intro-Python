# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__( self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

        # def view_name( self ):
        #     str
    def has_items(self):
        if len(self.items) > 0:
            print("Navy: HEY!")

    # def view_items(self):
    #         print("Items found in this room: \n")
    #         if len(self.items) == 0:
    #             print(" none")
    #         else:
    #             for i in self.items:
    #                 print("\t" + i.name)

    def view_items( self ):
        str_items = ("Items found in this room: \n")
        if len( self.items ) == 0:
            str_items += "\tnone"
        else:
            for i in self.items:
                str_items += "\t" + str(i) + "\n"
        return str_items


