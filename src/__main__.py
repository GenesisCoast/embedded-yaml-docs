import os
import sys
from pathlib import Path
from typing import List

import click
from jinja2 import Template
from pyfiglet import Figlet
from ruamel.yaml import YAML


from wrappers.ruamel_yaml_wrapper import RuamelYAMLWrapper
from yaml_docs_parser import YAMLDocsParser
from helpers.string_helper import StringHelper
from helpers.file_path_helper import FilePathHelper
from models.file import File


@click.group()
@click.version_option("1.0.0")
def main():
    f = Figlet(font='slant', justify='')
    print('EMBEDDED...')
    print(f.renderText("YAML Docs"))
    pass


@main.command()
@click.option('--search_path', help='Root folder to search for YAML files in.')
@click.option('--search_pattern', help='Search pattern to use when looking for YAML files.')
@click.option('--template_path', help='Path to the Jinja2 template.')
@click.option('--output_path', help='Folder path to output all the generated files to.')
@click.option('--recurse', is_flag=True, help='Gets the items in the specified locations and in all child items of the locations.')
def generate(
    search_path,
    search_pattern,
    template_path,
    output_path,
    recurse
):
    """

    """
    # Do we want to recursively search?
    if recurse:
        files = list(Path(search_path).rglob(search_pattern))
    else:
        files = list(Path(search_path).glob(search_pattern))

    # Prepare the libaries.
    yaml_parser = RuamelYAMLWrapper(YAML())
    docs_parser = YAMLDocsParser(yaml_parser)

    # Loop through each of the files and generate the docs.
    for f in files:
        # Get the file details.
        file = File(f)

        # Load the YAML file.
        yaml = yaml_parser.load_from_file(file.full_name)

        # Update the YAML file with docs using ByRef.
        docs_parser.extract_docs(yaml)

        # Process the template.
        template_object = open(template_path).read()
        template = Template(template_object)
        result = template.render(
            _file=file,
            _yaml=yaml
        )

        folder_structure = file.parent.replace(search_path, '')

        output_subfolder=FilePathHelper.join(
            output_path,
            folder_structure
        )

        os.makedirs(output_subfolder)

        output_file = output_subfolder = FilePathHelper.join(
            output_subfolder,
            file.name
        )

        with open(output_file, "x") as f:
            f.write(result)

if __name__ == '__main__':
    main()