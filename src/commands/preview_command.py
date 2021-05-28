
import os
import traceback

import click
from click.core import Context
from ruamel.yaml.parser import ParserError

from ..helpers.file_helper import FileHelper
from ..models.file_details import FileDetails


@click.group()
def preview():
    """
    Previews the documentation data that is passed into the Jinja2 template.
    """
    pass


@preview.command(name='file')
@click.pass_context
@click.option('-f', '--file', help='Path to the YAML file to generate the preview for.', required=True)
@click.option('-o', '--output', help='Filepath to save the preview to, if none is specified then ".preview" is appended to the original file name.', required=False)
@click.option('-pre', '--exclprefix', help='List of comment prefixes to exclude from the generated documentation.', multiple=True, required=False)
@click.option('-r', '--root', help='Root of your repository, used to create relative file paths.', required=False)
@click.option('-x', '--exit', help='Throw a terminating error if one of the templates fail.', is_flag=True, required=False)
@click.option('-w', '--overwrite', help='Overwrites any existing previews.', is_flag=True, required=False)
def prevfile(
    ctx: Context,
    file: str,
    output: str = None,
    exclprefix: list = None,
    root: str = None,
    exit: bool = False,
    overwrite: bool = False
):
    """
    Command used for, a preview of the documentation data that is passed into the Jinja2 template.
    """

    # Create a default for the output.
    if not output:
        output = FileHelper.exchange_file_extension(file, '.preview')

    # Make sure the paths are correct.
    os.path.isdir(file)
    os.path.isdir(output)

    template_error = False
    try:
        # Get the file details.
        details = FileDetails(file, root)

        # Read the contents of the file.
        with open(file) as f:
            contents = f.read()

        # Load the YAML file.
        try:
            yaml = ctx.obj.yaml.load(contents)
        except ParserError as e:
            print('There was an error in the YAML file.')
            raise

        # Make sure the prefix exclusion is a list.
        if not isinstance(exclprefix, list):
            exclprefix = [exclprefix]

        # Update the YAML file with docs using ByRef.
        print('Generating the preview for...')
        print(file)
        ctx.obj.docs.extract_docs(yaml, exclprefix)

        # Output the generated doc.
        try:
            print('\nOutputting the preview to...')
            print(output)

            mode = 'x'
            if overwrite:
                mode = 'w'

            with FileHelper.open_makedirs(output, mode) as f:
                f.write(ctx.obj.yaml.dump_str({
                    '_file': details,
                    '_contents': contents,
                    '_yaml': yaml
                }))

        except Exception as e:
            print('There was an error outputting the doc.')
            raise

    except Exception as e:
        print(f'Error at file "{file}"')
        print(e)
        print(traceback.format_exc())
        template_error = True

    print('\n')

    if exit and template_error:
        raise Exception('One of the templates failed to generate')


@preview.command(name='folder')
@click.pass_context
@click.option('-f', '--folder', help='Root folder to search for YAML files in.', required=True)
@click.option('-o', '--output', help='Folder path to output all the previews to. If none is specified then the search folder is used.', required=False)
@click.option('-s', '--search', help='Search pattern to use when looking for YAML files. Defaults to "*.yml".', required=False, default='*.yml')
@click.option('-pre', '--exclprefix', help='List of comment prefixes to exclude from the generated documentation.', multiple=True, required=False)
@click.option('-r', '--root', help='Root of your repository, used to create relative file paths. Defaults to the specified folder.', required=False)
@click.option('-x', '--exit', help='Throw a terminating error if one of the templates fail.', is_flag=True, required=False)
@click.option('-c', '--recurse', help='Gets the items in the specified locations and in all child items of the locations. False by default.', is_flag=True, required=False)
@click.option('-w', '--overwrite', help='Overwrites any existing previews.', is_flag=True, required=False)
def prevfolder(
    ctx: Context,
    folder: str,
    output: str = None,
    search: str = None,
    exclprefix: list = None,
    root: str = None,
    recurse: bool = False,
    exit: bool = False,
    overwrite: bool = False
):
    """
    Command used for, generating previews of the documentation data used in the Jinja2 template.
    For an entire folder of YAML files.
    """

    # Set the default values.
    if not output:
        output = folder

    if not root:
        root = folder

    # Validate the paths.
    os.path.isdir(folder)
    os.path.isdir(output)
    os.path.isdir(root)

    print(search)

    # Do we want to recursively search?
    files = FileHelper.get_files(folder, search, recurse)
    print(f'Found {len(files)} YAML files to generate previews for...\n')

    # If there are no files to process throw an error.
    if len(files) == 0:
        raise Exception('No files were found to generate the preview for. Double check your search pattern.')

    # Loop through each of the files and generate the docs.
    for idx, file in enumerate(files):

        print(f'[{idx + 1}/{len(files)}] - {file}\n')

        ctx.invoke(
            prevfile,
            file=file,
            output=FileHelper.exchange_file_extension(file, '.preview'),
            exclprefix=exclprefix,
            root=folder,
            exit=exit,
            overwrite=overwrite
        )
