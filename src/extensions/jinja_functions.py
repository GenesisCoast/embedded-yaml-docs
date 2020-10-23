from markupsafe import soft_str

class JinjaFunctions:

    @staticmethod
    def hasprop(obj: any, property: str) -> bool:
        """
        Checks if the object has a specific property.
        """
        return soft_str(property) in obj