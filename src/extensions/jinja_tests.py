import re
from markupsafe import soft_unicode


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
        return re.match(pattern, soft_unicode(value), flags)


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
        return soft_unicode(value).lower().startswith(prefix)


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
        return soft_unicode(value).lower().endswith(postfix)


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
        return soft_unicode(value).lower().startswith(prefix)


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
        return soft_unicode(value).lower().endswith(postfix)


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
        return substring in soft_unicode(value)


    @staticmethod
    def not_contains(value: any, substring: str) -> bool:
        """
        Tests if the value does not contain a substring.

        Parameters:
            value (str): The value to test.
            substring (str): Substring to test against.

        Returns:
            True if the value contains the supplied substring.
        """
        return not JinjaTests.contains(value, substring)


    @staticmethod
    def contains_times(value: any, substring: str, times: int) -> bool:
        """
        Tests if the the value contains the substring a certain amount of times.

        Parameters:
            value (str): The value to test.
            substring (str): Substring to test against.
            times (int): Number of substrings that should be present in the value.

        Returns:
            True if value contains the specified substring a certain amount of times.
        """
        return soft_unicode(value).count(substring) == int(times)


    @staticmethod
    def contains_gttimes(value: any, substring: str, greater_than: int) -> bool:
        """
        Tests if the number of occurrences of the substring in the value, is greater than
        the supplied number.

        Parameters:
            value (str): The value to test.
            substring (str): Substring to test against.
            greater_than (int): Number of substring occurrences that should be greater than.

        Returns:
            True if the number of substring occurrences is greater than the supplied number.
        """
        return soft_unicode(value).strip().count(substring) > int(greater_than)