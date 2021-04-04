from .item import Item


class Electronics(Item):
    def __init__(self, condition = None, edge = None):
        super().__init__(category = "Electronics", condition, edge)

    
    '''
    This function is created to customize the string representation 
    of this self instance.
    Python call __str__ method automatically when str() is called,
    then overrides its str() method to return "A gadget full of 
    buttons and secrets."
    '''
    def __str__(self):
        return "A gadget full of buttons and secrets."   



