import os

from ruamel.yaml import YAML
from ruamel.yaml.tokens import CommentToken
from ruamel.yaml.compat import StringIO


class RuamelYamlWrapper(YAML):
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


    def load_from_file(self, path: str) -> any:
        """

        """
        return super().load(open(path).read())


    def load_from_relative_file(self, rel_path: str, root: str) -> any:
        """

        """
        return self.load_from_file(
            os.path.join(
                root,
                rel_path
            )
        )