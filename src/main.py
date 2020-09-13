import os
import sys
from typing import Iterator, List, Tuple

from ruamel.yaml import YAML
import click
from jinja2 import Template
from pyfiglet import Figlet

from docs_processor import DocsProcessor
from ruamel_yaml_wrapper import RuamelYamlWrapper
from models.file import File
from custom_loader import Hero


from pathlib import Path, WindowsPath

f = Figlet(font='slant', justify='')
print(f.renderText("Embedded YAML Docs"))


# @click.command()
# @click.option('--path', help='Specifies a location to search for YAML files in. Defaults to the current directory')
# @click.option('--search_pattern', help='Specifies a search pattern to use when looking for YAML files.')
# @click.option('--recurse', is_flag=True, help='Gets the items in the specified locations and in all child items of the locations.')
def main(path, search_pattern, recurse):
    """

    """
    # Do we want to recursively search?
    if recurse:
        files = list(Path(path).rglob(search_pattern))
    else:
        files = list(Path(path).glob(search_pattern))

    # Prepare the libaries.
    parser = RuamelYamlWrapper()

    # Loop through each of the files and generate the docs.
    for f in files:
        # Get the file details.
        file = File(f)

        # Load the YAML file.
        yaml = parser.load_from_file(file.full_name)

        # Update the YAML file with docs using ByRef.
        parser.get_yaml_comments(yaml)

        # Process the template.
        template_object = open('src/templates/azure_devops/azdo_pipeline_template.jin').read()
        template = Template(template_object)
        result = template.render(
            _file=file,
            _yaml=yaml
        )
        print(result)

if __name__ == "__main__":
    main(r'C:\Git Repos\embedded-yaml-docs\src\examples\azure_devops', '*.yml', True)