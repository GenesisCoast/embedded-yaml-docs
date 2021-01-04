import re

from .string_helper import StringHelper


class YAMLCommentHelper:
    """
    Collection of helper methods to be used with YAML comments.
    """


    @staticmethod
    def format_comment(comment: str) -> str:
        """
        Formats the comment by removing the YAML comment indicator '#',
        and removing newlines/blanks spaces from either sides of the string.

        Parameters:
            comment (str): The comment to format.

        Returns:
            str: Returns the formatted comment.
        """
        # Remove stray newlines.
        comment = StringHelper.remove_prefix(comment, '\n')
        comment = StringHelper.remove_postfix(comment, '\n')

        # Check we are not stripping comment indentation.
        if comment.strip().startswith('#'):
            comment = comment.strip()

        # Remove the comment identifier.
        comment = StringHelper.remove_prefix(comment, '# ')

        return comment


    @staticmethod
    def format_comment_lines(comment):
        """

        """
        lines = list()

        for line in comment.split('\n'):
            lines.append(YAMLCommentHelper.format_comment(line))

        return '\n'.join(lines)