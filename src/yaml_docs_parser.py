import os
from typing import Iterator, List, Tuple, Final

from ruamel.yaml import YAML, safe_load
from ruamel.yaml.comments import CommentedSeq
from ruamel.yaml.compat import StringIO

from helpers.string_helper import StringHelper


class YAMLDocsParser(YAML):
    """
    Custom implementation of the ruamel library.
    """


    def dump_str(self, data: any, **kwargs) -> str:
        """
        Return the YAML object as a string.

        Properties:
            data<any>: The YAML object.
            options: Options for the YAML dump.

        Returns:
            The YAML object as a string.
        """
        stream = StringIO()

        super().dump(data, stream, **kwargs)

        output_str = stream.getvalue()

        stream.close()

        return output_str


    def load(self, stream) -> any:
        """

        """
        return super().load(stream)


    def load_from_file(self, path: str) -> any:
        """

        """
        return self.load(open(path).read())


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
        comment_block_lines = []

        # Iterate through each of the comments.
        for comment in token:
            # Check the comment is not NULL.
            if comment is not None:
                if not isinstance(comment, list):
                    # Format the initial comment.
                    comment_value = self.format_comment(comment.value)
                    comment_value = self.format_comment_lines(comment_value)
                    comment_block_lines.append(comment_value)
                else:
                    for sub_comment in comment:
                        if sub_comment is not None:
                            # Format the initial comment.
                            sub_comment_value = self.format_comment(sub_comment.value)
                            sub_comment_value = self.format_comment_lines(sub_comment_value)
                            comment_block_lines.append(sub_comment_value)

        # Yield the comment
        comment_block = "\n".join(comment_block_lines or list())

        yield safe_load(comment_block)


    def get_yaml_comments(self, section, parent=None) -> Iterator[Tuple[any, Tuple[any, str]]]:
        """
        Recursively extracts the YAML comments from the YAML section. For all the YAML properties.

        Parameters:
            section (any): The YAML section to extract all the comments for.
            parent (any): The parent to the current section. Used to determine behaviour.
                If value is set to 'None' then function assumes that it is currently
                executing at the root of the YAML doc.

        Links:
            https://stackoverflow.com/questions/55130078/yaml-parsing-with-comments-for-doc-purpose

        Returns:
            Iterator[Tuple[any, Tuple[any, str]]]: Value generator that contains both the
            supplied section and a Tuple; that contains the corresponding YAML token
            and extracted comment.
        """
        DOCS_PROPERTY_NAME: Final = 'docs'

        # Extract the comments for a dictionary section.
        if isinstance(section, dict):
            # Get inline comments
            # if section.ca.comment is not None:
            #     for comment in extract_comment_from_token(section.ca.comment):
            #         yield section, comment

            # Loop through all the keys in the dictionary.
            for key in section.keys():
                # Localize the value, done to avoid 'OrderedDict mutated during iteration'.
                val = section[key]

                # Drill down to get the nested comments, for complex values.
                self.get_yaml_comments(val, section)

                # Check for a comment in the YAML (iteration) object.
                if isinstance(val, CommentedSeq):
                    # Is there a comment?
                    if val.ca.items:
                        for comment in self.extract_comment_from_token(val.ca.items[0]):
                            section[key].docs = comment
                    else:
                        section[key].docs = None

                # Check if we are currently at the root, or the section is a
                # list of YAML objects (CommentedSeq).
                if parent is None or not isinstance(parent, CommentedSeq):
                    # Re-initialize the 'key: str' pair with a new dict to hold
                    # both the value and docs; 'key: { value: str, docs: {} }'.
                    if isinstance(val, str):
                        section[key] = {
                            'name': key,
                            'value': val
                        }

                # Are there key specific comments?
                if key in section.ca.items:
                    for comment in self.extract_comment_from_token(section.ca.items[key]):
                        # Check if we are currently at the root, or the section is a
                        # list of YAML objects (CommentedSeq
                        if parent is None or not isinstance(parent, CommentedSeq):
                            # Add the docs to the 'key: str' pair. The pair is re-initialized
                            # above so that the structure is consistent; 'key: { value: str, docs: {} }'.
                            if isinstance(val, str):
                                section[key][DOCS_PROPERTY_NAME] = comment
                        else:
                            if not isinstance(val, dict):
                                section[DOCS_PROPERTY_NAME] = comment

        # Extract the comments for a list section.
        elif isinstance(section, list):
            # Iterate through all the items in the YAML list.
            for index, item in enumerate(section):
                # Drill down to get the nested comments, for complex values.
                self.get_yaml_comments(item, section)

                # If item is a string re-initialize it with a new dict to hold
                # both the value and the docs.
                if isinstance(item, str):
                    section[index] = {
                        'value': item
                    }

                # TODO: Test if this can be removed? See corresponding section
                # TODO: 'Check for a comment in the YAML (iteration) object.'
                # for comment in self.get_yaml_comments(item):
                #     yield section

                # Are there item specific comments?
                if index in section.ca.items:
                    for comment in self.extract_comment_from_token(section.ca.items[index]):
                        if DOCS_PROPERTY_NAME not in section[index]:
                            section[index][DOCS_PROPERTY_NAME] = comment
