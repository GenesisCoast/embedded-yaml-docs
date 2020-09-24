import re


class JinjaTests:
    """
    Collection of custom Jinja Tests.
    """


    @staticmethod
    def regex_match(value: any, pattern: str, flags: int=0) -> bool:
        """
        Tests if the value matches the supplied regex pattern.

        Parameters:
            value (any): The value to test.
            pattern (str): Regex pattern to test against.
            flags (int): Any specific regex flags.

        Returns:
            True if the value matches the regex pattern, else false.
        """
        return re.match(pattern, str(value), flags)


    @staticmethod
    def startswith(value: any, prefix: str) -> bool:
        """
        Tests if the value startswith the supplied prefix.

        Parameters:
            value (str): The value to test.
            prefix (str): Prefix to test against.

        Returns:
            True if the value startswith the supplied prefix.
        """
        return str(value).lower().startswith(prefix)


    @staticmethod
    def endswith(value: any, postfix: str) -> bool:
        """
        Tests if the value endswith the supplied postfix.

        Parameters:
            value (str): The value to test.
            postfix (str): Postfix to test against.

        Returns:
            True if the value endswith the supplied postfix.
        """
        return str(value).lower().endswith(postfix)


    @staticmethod
    def not_startswith(value: any, prefix: str) -> bool:
        """
        Tests if the value does not startswith the supplied prefix.

        Parameters:
            value (str): The value to test.
            prefix (str): Prefix to test against.

        Returns:
            False if the value startswith the supplied prefix.
        """
        return str(value).lower().startswith(prefix)


    @staticmethod
    def not_endswith(value: any, postfix: str) -> bool:
        """
        Tests if the value does not endswith the supplied postfix.

        Parameters:
            value (str): The value to test.
            postfix (str): Postfix to test against.

        Returns:
            False if the value endswith the supplied postfix.
        """
        return str(value).lower().endswith(postfix)


    @staticmethod
    def contains(value: any, substring: str) -> bool:
        """
        Tests if the value contains a substring.

        Parameters:
            value (str): The value to test.
            substring (str): Substring to test against.

        Returns:
            True if the value contains the supplied substring.
        """
        return substring in str(value)