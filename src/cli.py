import click
from click import Context
from pyfiglet import Figlet

from .commands.generate_command import generate
from .commands.preview_command import preview
from .jinja2.jinja2_environment import Jinja2Environment
from .parser import YAMLDocsParser
from .wrappers.ruamel_yaml_wrapper import RuamelYAMLWrapper


class DependencyContainer:
    """
    Container for storing all the dependency injections for the app.
    """

    def __init__(
        self,
        yaml: RuamelYAMLWrapper,
        docs: YAMLDocsParser
    ):
        self.yaml = yaml
        self.docs = docs
        self.jinja2 = Jinja2Environment()


@click.group(invoke_without_command=True)
@click.version_option("1.0.0")
@click.pass_context
def cli(ctx: Context):
    """
    CLI used for generating documentation, based on the comments in your YAML file.
    """

    print('EMBEDDED...')

    f = Figlet(font='slant', justify='')
    print(f.renderText("YAML Docs"))

    yaml = RuamelYAMLWrapper()

    ctx.obj = DependencyContainer(
        yaml=yaml,
        docs=YAMLDocsParser(yaml)
    )


cli.add_command(generate)
cli.add_command(preview)


if __name__ == '__main__':
    cli()
