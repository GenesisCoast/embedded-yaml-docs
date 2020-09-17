class StringHelper:
    """
    Collection of helper methods for the string datatype.
    """

    @staticmethod
    def startswith_multi(text: str, *prefixes: list) -> bool:
        """

        """
        for prefix in prefixes:
            if text.startswith(prefix):
                return True
        return False


    @staticmethod
    def remove_prefix(text: str, prefix: str) -> str:
        """
        Removes the specified prefix from the text.

        Parameters:
            text (str): Text to remove the prefix from.
            prefix (str): Prefix to remove from the text.

        Returns:
            str: The text minus the specified prefix.
        """
        if text.startswith(prefix):
            return text[len(prefix):]
        return text


    @staticmethod
    def remove_postfix(text, postfix):
        """
        Removes the specified postfix from the text.

        Parameters:
            text (str): Text to remove the postfix from.
            postfix (str): postfix to remove from the text.

        Returns:
            str: The text minus the specified postfix.
        """
        if text.endswith(postfix):
            return text[: - (len(postfix))]
        return text
