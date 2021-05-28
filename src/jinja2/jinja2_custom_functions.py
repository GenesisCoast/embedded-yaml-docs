from markupsafe import soft_str


class Jinja2CustomFunctions:
    """
    Collection of custom Jinja Functions.
    """


    @staticmethod
    def do_hasprop(obj: any, property: str) -> bool:
        """
        Checks if the object has a specific property.

        Parameters:
            obj (any): The object to check the properties of.
            property (str): Name of the property to check the object has.

        Returns:
            (bool): Returns True if the object has the specified property,
                otherwise False.
        """
        return soft_str(property) in obj
