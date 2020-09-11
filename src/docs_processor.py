from ruamel.yaml import YAML
from typing import Tuple, Iterator, List
from helpers.string_helper import StringHelper

class DocsProcessor:
    """

    """


    def __init__(self, yaml_wrapper):
        """

        """
        self.__yaml_wrapper = yaml_wrapper


    def format_comment(self, comment: str) -> str:
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


    def format_comment_lines(self, comment):
        """

        """
        lines = list()

        for line in comment.split('\n'):
            lines.append(self.format_comment(line))

        return '\n'.join(lines)


    def extract_comment_from_token(self, token: any) -> Iterator[Tuple[any, str]]:
        """
        Extracts the comments from the supplied YAML token, and then yields the comment
        back to the caller (alongside the YAML token).

        Parameters:
            token (any): The YAML token to extract the comment for.

        Returns:
            Iterator[Tuple[any, str]]: Value generator that contains the YAML token and the
            extracted comment.
        """
        # Initialize a variable to store the comment block details.
        comment_block = []

        # Iterate through each of the comments.
        for comment in token:
            # Check the comment is not NULL.
            if comment is not None:
                # Format the initial comment.
                comment_value = self.format_comment(comment.value)
                comment_value = self.format_comment_lines(comment_value)
                comment_block.append(comment_value)

        # Yield the comment
        yield "\n".join(comment_block or list())


    def get_yaml_comments(self, section) -> Iterator[Tuple[any, Tuple[any, str]]]:
        """
        Extracts the YAML comments from the YAML section. For all the YAML properties.

        Parameters:
            section (any): The YAML section to extract all the comments for.

        Returns:
            Iterator[Tuple[any, Tuple[any, str]]]: Value generator that contains both the
            supplied section and a Tuple; that contains the corresponding YAML token
            and extracted comment.
        """
        if isinstance(section, dict):
            # Handle the root of a file.
            # if section.ca.comment is not None:
            #     for comment in extract_comment_from_token(section.ca.comment):
            #         yield section, comment

            for key, val in section.items():

                for comment in self.get_yaml_comments(val):
                    yield section, comment

                if key in section.ca.items:
                    for comment in self.extract_comment_from_token(section.ca.items[key]):
                        yield section, comment

        # To handle lists
        elif isinstance(section, list):

            # if section.ca.comment is not None:
            #     for comment in extract_comment_from_token(section.ca.comment):
            #         yield section, comment

            for idx, item in enumerate(section):

                for comment in self.get_yaml_comments(item):
                    yield section, comment

                if idx in section.ca.items:
                    for comment in self.extract_comment_from_token(section.ca.items[idx]):
                        yield section, comment


    def get_section_docs(self, section: any):
        """
        Extracts the documentation from the YAML sections comments, and returns them in a
        format that can be used.

        Parameters:
            section (any): The YAML section to get the documentation for.

        Returns:
            dict: A dictionary for each of the YAML tokens and their corresponding documentation.
        """
        tokens_with_comments = list()

        # Process all the extracted documentation.
        for source, item in self.get_yaml_comments(section):
            # Localize the token details.
            token = item[0]

            # Localize the docs for the token.
            docs = self.__yaml_wrapper.load(item[1])

            # Combine the token and documentation.
            if isinstance(docs, dict):
                # Make all the keys lowercase.
                docs = {k.lower(): v for k, v in docs.items()}

                # Combine the two dicts together, items in token will override doc keys.
                tokens_with_comments.append({ **docs, **token })
            else:
                # Combine the token items, with the description.
                tokens_with_comments.append({
                    **token,
                    'description': docs
                })

        return tokens_with_comments