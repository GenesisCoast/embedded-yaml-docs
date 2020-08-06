class StringHelper:
    """

    """

    @staticmethod
    def remove_prefix(text, prefix):
        """
        """
        if text.startswith(prefix):
            return text[len(prefix):]
        return text

    @staticmethod
    def remove_postfix(text, postfix):
        """
        """
        if text.endswith(postfix):
            return text[: - (len(postfix))]
        return text