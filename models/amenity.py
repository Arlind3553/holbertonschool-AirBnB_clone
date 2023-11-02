#!/usr/bin/python3
    """
    Amenity class that inherits from BaseModel
    """
class Amenity(BaseModel):
    """
    A class variable for 'name' with an initial value of an empty string
    """
    name = ""
    
    def __init__(self, *args, **kwargs):
        """
        Initialize a Amenity instance. Inherits initialization from BaseModel.
        """
        super().__init__(*args, **kwargs)
