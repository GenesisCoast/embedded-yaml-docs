import os
import sys
from operator import xor
from pathlib import Path
from typing import List

import click
from jinja2 import Template
from pyfiglet import Figlet
from ruamel.yaml import YAML
from ruamel.yaml.parser import ParserError

from .helpers.file_helper import FileHelper
from .models.file_details import FileDetails
from .wrappers.ruamel_yaml_wrapper import RuamelYAMLWrapper
from .yaml_docs_parser import YAMLDocsParser


@click.group()
@click.version_option("1.0.0")
def main():
    f = Figlet(font='slant', justify='')
    print('EMBEDDED...')
    print(f.renderText("YAML Docs"))
    pass


@main.command()
@click.option(
    '-p',
    '--path',
    'path',
    help='Root folder to search for YAML files in.',
    required=True,
    type=str
)
@click.option(
    '-a',
    '--pattern',
    'pattern',
    help='Search pattern to use when looking for YAML files.',
    required=True,
    type=str
)
@click.option(
    '-t',
    '--template-path',
    'template_path',
    help='Path to the Jinja2 template.',
    required=True,
    type=str
)
@click.option(
    '-o',
    '--output-path',
    'output_path',
    help='Folder path to output all the generated files to.',
    required=True,
    type=str
)
@click.option(
    '-e',
    '--exclude-comments',
    'exclude_comments',
    help='List of comment prefixes to exclude from the generated documentation.',
    multiple=True,
    required=False
)
@click.option(
    '-r',
    '--recurse',
    'recurse',
    help='Gets the items in the specified locations and in all child items of the locations. False by default.',
    is_flag=True,
    required=False
)
@click.option(
    '-w',
    '--overwrite',
    'overwrite',
    help='Overwrites any existing documents.',
    is_flag=True,
    required=False
)
def generate(
    path: str,
    pattern: str,
    template_path: str,
    output_path: str,
    exclude_comments: list=None,
    recurse: bool = False,
    overwrite: bool = False
):
    """

    """
    # Check if the paths are in the correct format.
    if xor(os.path.isfile(path), os.path.isfile(output_path)):
        raise 'The "path" and "output_path" must either be both a file path or a directory path.'

    # Prepare the libaries.
    yaml_parser = RuamelYAMLWrapper(YAML())
    docs_parser = YAMLDocsParser(yaml_parser)

    # Do we want to recursively search?
    files = FileHelper.get_files(path, pattern, recurse)
    print(f'Found {len(files)} YAML files to generate the docs for...\n')

    # If there are no files to process throw an error.
    if len(files) == 0:
        raise 'No files were found to generate docs for. Double check your search pattern.'

    # Loop through each of the files and generate the docs.
    for idx, file in enumerate(files):
        try:
            # Get the file details.
            fd = FileDetails(file, output_path, path)
            print(f'[{idx + 1}/{len(files)}] - {fd.rel_full_name}')

            # Load the YAML file.
            try:
                yaml = yaml_parser.load_from_file(fd.full_name)
            except ParserError as e:
                print('There was an error in the YAML file.')
                raise

            # Update the YAML file with docs using ByRef.
            print('Generating the docs...')
            docs_parser.extract_docs(yaml, exclude_comments)

            # Render the doc file using the template.
            try:
                template_object = open(template_path).read()
                template = Template(template_object)

                result = template.render(
                    _file=file,
                    _yaml=yaml
                )
            except Exception as e:
                print('There was an error with the supplied jinja2 template...')
                raise

            # Output the generated doc.
            try:
                print(f'Outputting the docs...')

                output_file=FileHelper.join_paths(
                    output_path,
                    fd.rel_parent,
                    fd.name_without_suffix + '.md'
                )

                mode = 'x'
                if overwrite:
                    mode = 'w'

                with FileHelper.open_makedirs(output_file, mode) as f:
                    f.write(result)

            except Exception as e:
                print('There was an error outputting the doc.')
                raise

        except Exception as e:
            print(f'Error at file "{fd.full_name}"')
            print(e)

        print('\n')


if __name__ == '__main__':
    main()