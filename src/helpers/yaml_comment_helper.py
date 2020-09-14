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
        comment = StringHelper.remove_prefix(comment, '\n')
        comment = StringHelper.remove_postfix(comment, '\n')
        comment = comment.strip()
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