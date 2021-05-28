import re
from markupsafe import soft_unicode


class Jinja2CustomTests:
    """
    Collection of custom Jinja Tests.
    """


    @staticmethod
    def do_contains(value: any, substring: str) -> bool:
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
    def do_contains_times(value: any, substring: str, times: int) -> bool:
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
    def do_contains_gttimes(value: any, substring: str, greater_than: int) -> bool:
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


    @staticmethod
    def do_endswith(value: any, postfix: str) -> bool:
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
    def do_not_contains(value: any, substring: str) -> bool:
        """
        Tests if the value does not contain a substring.

        Parameters:
            value (str): The value to test.
            substring (str): Substring to test against.

        Returns:
            False if the value contains the supplied substring.
        """
        return not Jinja2CustomTests.do_contains(value, substring)


    @staticmethod
    def do_not_endswith(value: any, postfix: str) -> bool:
        """
        Tests if the value does not endswith the supplied postfix.

        Parameters:
            value (str): The value to test.
            postfix (str): Postfix to test against.

        Returns:
            False if the value endswith the supplied postfix.
        """
        return not Jinja2CustomTests.do_endswith(value, postfix)


    @staticmethod
    def do_not_startswith(value: any, prefix: str) -> bool:
        """
        Tests if the value does not startswith the supplied prefix.

        Parameters:
            value (str): The value to test.
            prefix (str): Prefix to test against.

        Returns:
            False if the value startswith the supplied prefix.
        """
        return Jinja2CustomTests.do_startswith(value, prefix)


    @staticmethod
    def do_not_regexmatch(value: any, pattern: str, flags: int=0) -> bool:
        """
        Tests if the value does not matche the supplied regex pattern.

        Parameters:
            value (any): The value to test.
            pattern (str): Regex pattern to test against.
            flags (int): Any specific regex flags.

        Returns:
            False if the value matches the regex pattern, else false.
        """
        return not Jinja2CustomTests.do_regexmatch(value, pattern, flags)


    @staticmethod
    def do_regexmatch(value: any, pattern: str, flags: int=0) -> bool:
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
    def do_startswith(value: any, prefix: str) -> bool:
        """
        Tests if the value startswith the supplied prefix.

        Parameters:
            value (str): The value to test.
            prefix (str): Prefix to test against.

        Returns:
            True if the value startswith the supplied prefix.
        """
        return soft_unicode(value).lower().startswith(prefix)
