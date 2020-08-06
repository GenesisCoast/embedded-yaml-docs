import sys
import os

from wrappers.ruamel_yaml_wrapper import RuamelYamlWrapper
from helpers.string_helper import StringHelper


def extract_comment_from_token(token):
    # Initialize a variable to store the comment block details.
    comment_block = []

    # Iterate through each of the comments.
    for comment in token:
        # Check the comment is not NULL.
        if comment is not None and isinstance(comment, list):
            # Iterate through each of the lines in the comment.
            for comment_line in comment:
                # Check the comment line is not NULL.
                if comment_line is not None:
                    # Format the comment.
                    comment_line_value = comment_line.value
                    comment_line_value = StringHelper.remove_prefix(comment_line_value, '# ')
                    comment_line_value = StringHelper.remove_postfix(comment_line_value, '\n')
                    comment_block.append(comment_line_value)

    # Yield the comment
    yield "\n".join(comment_block)


def get_yaml_comments(d):
    if isinstance(d, dict):
        # Handle the root of a file.
        if d.ca.comment is not None:
            for comment in extract_comment_from_token(d.ca.comment):
                yield d, comment

        for key, val in d.items():

            for comment in get_yaml_comments(val):
                yield d, comment

            if key in d.ca.items:
                for comment in extract_comment_from_token(d.ca.items[key]):
                    yield d, comment

    elif isinstance(d, list):

        if d.ca.comment is not None:
            for comment in extract_comment_from_token(d.ca.comment):
                yield d, comment

        for idx, item in enumerate(d):

            for comment in get_yaml_comments(item):
                yield d, comment

            if idx in d.ca.items:
                for comment in extract_comment_from_token(d.ca.items[idx]):
                    yield d, comment


script_dir = os.path.dirname(__file__)
yaml = RuamelYamlWrapper()
data = yaml.load_from_relative_file('examples/azure_devops/azdo_variables_pipeline.yml', script_dir)

for d, comment in get_yaml_comments(data['variables']):
    print(f"{comment!r}")