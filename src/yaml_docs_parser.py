import os
import re
from typing import Iterator, List, Tuple

from ruamel.yaml.comments import CommentedSeq

from .helpers.string_helper import StringHelper
from .helpers.yaml_comment_helper import YAMLCommentHelper
from .wrappers.ruamel_yaml_wrapper import RuamelYAMLWrapper


class YAMLDocsParser():
    """

    """


    def __init__(self, yaml_parser: RuamelYAMLWrapper,):
        """

        """
        self._yaml_parser = yaml_parser



    def __get_token_from_comment(self, token: any, exclude_comments:list = None) -> Iterator[Tuple[any, str]]:
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
                    comment_value = YAMLCommentHelper.format_comment(comment.value)
                    comment_value = YAMLCommentHelper.format_comment_lines(comment_value)
                    comment_block_lines.append(comment_value)
                else:
                    for sub_comment in comment:
                        if sub_comment is not None:
                            # Format the initial comment.
                            sub_comment_value = YAMLCommentHelper.format_comment(sub_comment.value)
                            sub_comment_value = YAMLCommentHelper.format_comment_lines(sub_comment_value)
                            comment_block_lines.append(sub_comment_value)

        # Yield the comment
        comment_block = "\n".join(comment_block_lines or list())

        # Return the parsed documentation.
        if exclude_comments:
            if not StringHelper.startswith_multi(comment_block, exclude_comments):
                yield self._yaml_parser.safe_load(comment_block)


    def extract_docs(
        self,
        section,
        exclude_comment_prefixes=None,
        parent=None,
        property_name: str = 'docs',
    ) -> Iterator[Tuple[any, Tuple[any, str]]]:
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
        # Extract the comments for a dictionary section.
        if isinstance(section, dict):
            # Loop through all the keys in the dictionary.
            for key in section.keys():
                # Localize the value, done to avoid 'OrderedDict mutated during iteration'.
                val = section[key]

                # Drill down to get the nested comments, for complex values.
                self.extract_docs(val, parent=section)

                # Check for a comment in the YAML (iteration) object.
                if isinstance(val, CommentedSeq):
                    # Is there a comment?
                    if val.ca.items and '0' in val.ca.items:
                        for comment in self.__get_token_from_comment(val.ca.items[0], exclude_comments):
                            section[key][property_name] = comment
                    # else:
                    #     section[key][property_name] = None

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

                # Is there a comments section?
                if 'ca' in section:
                    # Are there key specific comments?
                    if key in section.ca.items:
                        for comment in self.__get_token_from_comment(section.ca.items[key], exclude_comments):
                            # Check if we are currently at the root, or the section is a
                            # list of YAML objects (CommentedSeq
                            if parent is None or not isinstance(parent, CommentedSeq):
                                # Add the docs to the 'key: str' pair. The pair is re-initialized
                                # above so that the structure is consistent; 'key: { value: str, docs: {} }'.
                                if isinstance(val, str):
                                    section[key][property_name] = comment
                            else:
                                if not isinstance(val, dict):
                                    section[property_name] = comment

        # Extract the comments for a list section.
        elif isinstance(section, list):
            # Iterate through all the items in the YAML list.
            for index, item in enumerate(section):
                # Drill down to get the nested comments, for complex values.
                self.extract_docs(item, parent=section)

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
                    for comment in self.__get_token_from_comment(section.ca.items[index], exclude_comments):
                        if property_name not in section[index]:
                            section[index][property_name] = comment

        # Get inline comments
        if parent is None and isinstance(section, dict):
            if section.ca.comment is not None:
                for comment in self.__get_token_from_comment(section.ca.comment, exclude_comments):
                    section[property_name] = comment