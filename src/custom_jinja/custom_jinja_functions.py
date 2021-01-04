from markupsafe import soft_str


class CustomJinjaFunctions:
    """
    Collection of custom Jinja Functions.
    """


    @staticmethod
    def do_hasprop(obj: any, property: str) -> bool:
        """
        Checks if the object has a specific property.
        """
        return soft_str(property) in obj